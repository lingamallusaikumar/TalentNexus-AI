from app.common.models import BaseModel
from app.extensions import db

class SkillCategory(BaseModel):
    __tablename__ = 'skill_categories'

    name = db.Column(db.String(64), unique=True, nullable=False, index=True)
    description = db.Column(db.String(255), nullable=True)
    
    skills = db.relationship('Skill', backref='category', lazy=True)

class Skill(BaseModel):
    __tablename__ = 'skills'

    name = db.Column(db.String(64), unique=True, nullable=False, index=True)
    slug = db.Column(db.String(64), unique=True, nullable=False, index=True)
    category_id = db.Column(db.Integer, db.ForeignKey('skill_categories.id', ondelete='SET NULL'), nullable=True, index=True)
    parent_skill_id = db.Column(db.Integer, db.ForeignKey('skills.id', ondelete='SET NULL'), nullable=True, index=True)
    
    is_standard = db.Column(db.Boolean, default=True) # Standard curated taxonomy vs user-added
    demand_count = db.Column(db.Integer, default=0) # Tracks occurrences in active job descriptions
    
    # Sub-skills / Hierarchy
    sub_skills = db.relationship('Skill', backref=db.backref('parent_skill', remote_side='Skill.id'), lazy=True)
    aliases = db.relationship('SkillAlias', backref='canonical_skill', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Skill {self.name}>"

class SkillAlias(BaseModel):
    __tablename__ = 'skill_aliases'

    alias = db.Column(db.String(64), unique=True, nullable=False, index=True) # e.g. JS, Py, Postgres, ReactJS
    canonical_skill_id = db.Column(db.Integer, db.ForeignKey('skills.id', ondelete='CASCADE'), nullable=False, index=True)

class SkillRelationship(BaseModel):
    """Represents cross-skill graphs e.g. Flask related to Python with weight 0.9"""
    __tablename__ = 'skill_relationships'

    source_skill_id = db.Column(db.Integer, db.ForeignKey('skills.id', ondelete='CASCADE'), nullable=False, index=True)
    target_skill_id = db.Column(db.Integer, db.ForeignKey('skills.id', ondelete='CASCADE'), nullable=False, index=True)
    relation_type = db.Column(db.String(32), default='RELATED_TO') # PARENT_OF, FRAMEWORK_FOR, TOOL_FOR, RELATED_TO
    similarity_weight = db.Column(db.Float, default=0.5)

    source = db.relationship('Skill', foreign_keys=[source_skill_id])
    target = db.relationship('Skill', foreign_keys=[target_skill_id])

    __table_args__ = (
        db.UniqueConstraint('source_skill_id', 'target_skill_id', name='uq_skill_relation'),
    )
