from app.common.models import BaseModel
from app.extensions import db

class Candidate(BaseModel):
    __tablename__ = 'candidates'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)
    phone = db.Column(db.String(32), nullable=True)
    summary = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(128), nullable=True)
    linkedin_url = db.Column(db.String(255), nullable=True)
    github_url = db.Column(db.String(255), nullable=True)
    portfolio_url = db.Column(db.String(255), nullable=True)
    
    # Relationships
    user = db.relationship('User', backref=db.backref('candidate_profile', uselist=False))
    experiences = db.relationship('Experience', backref='candidate', cascade="all, delete-orphan")
    educations = db.relationship('Education', backref='candidate', cascade="all, delete-orphan")
    skills = db.relationship('CandidateSkill', backref='candidate', cascade="all, delete-orphan")

class Experience(BaseModel):
    __tablename__ = 'experiences'

    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id'), nullable=False)
    company = db.Column(db.String(128), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    location = db.Column(db.String(128), nullable=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=True)
    is_current = db.Column(db.Boolean, default=False)
    description = db.Column(db.Text, nullable=True)

class Education(BaseModel):
    __tablename__ = 'educations'

    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id'), nullable=False)
    institution = db.Column(db.String(128), nullable=False)
    degree = db.Column(db.String(128), nullable=False)
    field_of_study = db.Column(db.String(128), nullable=True)
    start_date = db.Column(db.Date, nullable=True)
    end_date = db.Column(db.Date, nullable=True)
    gpa = db.Column(db.String(16), nullable=True)

class CandidateSkill(BaseModel):
    __tablename__ = 'candidate_skills'

    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id'), nullable=False)
    # This will link to a global Skill master table later, for now we just use a string name
    skill_name = db.Column(db.String(64), nullable=False)
    years_of_experience = db.Column(db.Float, nullable=True)
    confidence_score = db.Column(db.Float, nullable=True) # Extracted by AI
