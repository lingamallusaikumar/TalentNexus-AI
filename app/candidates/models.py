from app.common.models import BaseModel, SoftDeleteMixin
from app.extensions import db

class Candidate(BaseModel, SoftDeleteMixin):
    __tablename__ = 'candidates'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, unique=True, index=True)
    first_name = db.Column(db.String(64), nullable=True)
    last_name = db.Column(db.String(64), nullable=True)
    headline = db.Column(db.String(128), nullable=True) # e.g. Senior Backend Architect | Python | ML
    phone = db.Column(db.String(32), nullable=True, index=True)
    email = db.Column(db.String(128), nullable=True, index=True)
    location = db.Column(db.String(128), nullable=True, index=True)
    country = db.Column(db.String(64), nullable=True)
    city = db.Column(db.String(64), nullable=True)
    postal_code = db.Column(db.String(16), nullable=True)
    
    summary = db.Column(db.Text, nullable=True)
    years_of_experience = db.Column(db.Float, default=0.0, index=True)
    highest_education_level = db.Column(db.String(64), nullable=True) # Bachelor, Master, PhD
    
    # Portfolio & Social links
    linkedin_url = db.Column(db.String(255), nullable=True)
    github_url = db.Column(db.String(255), nullable=True)
    portfolio_url = db.Column(db.String(255), nullable=True)
    website_url = db.Column(db.String(255), nullable=True)
    
    # AI Profile Insights
    resume_quality_score = db.Column(db.Float, default=0.0, index=True) # 0 to 100
    quality_breakdown = db.Column(db.JSON, nullable=True)
    profile_embedding = db.Column(db.JSON, nullable=True) # dense vector stored as JSON array
    is_duplicate = db.Column(db.Boolean, default=False, index=True)
    primary_candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id', ondelete='SET NULL'), nullable=True)

    # Relationships
    user = db.relationship('User', backref=db.backref('candidate_profile', uselist=False, cascade="all, delete-orphan"))
    experiences = db.relationship('Experience', backref='candidate', cascade="all, delete-orphan", order_by="desc(Experience.start_date)")
    educations = db.relationship('Education', backref='candidate', cascade="all, delete-orphan", order_by="desc(Education.start_date)")
    skills = db.relationship('CandidateSkill', backref='candidate', cascade="all, delete-orphan")
    certifications = db.relationship('CandidateCertification', backref='candidate', cascade="all, delete-orphan")
    languages = db.relationship('CandidateLanguage', backref='candidate', cascade="all, delete-orphan")
    projects = db.relationship('CandidateProject', backref='candidate', cascade="all, delete-orphan")
    tags = db.relationship('CandidateTag', backref='candidate', cascade="all, delete-orphan")
    notes = db.relationship('CandidateNote', backref='candidate', cascade="all, delete-orphan")
    activities = db.relationship('CandidateActivity', backref='candidate', cascade="all, delete-orphan", order_by="desc(CandidateActivity.created_at)")

class Experience(BaseModel):
    __tablename__ = 'experiences'

    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id', ondelete='CASCADE'), nullable=False, index=True)
    company = db.Column(db.String(128), nullable=False, index=True)
    title = db.Column(db.String(128), nullable=False, index=True)
    location = db.Column(db.String(128), nullable=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=True)
    is_current = db.Column(db.Boolean, default=False, nullable=False)
    description = db.Column(db.Text, nullable=True)
    achievements = db.Column(db.JSON, default=list) # List of bullet points

class Education(BaseModel):
    __tablename__ = 'educations'

    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id', ondelete='CASCADE'), nullable=False, index=True)
    institution = db.Column(db.String(128), nullable=False, index=True)
    degree = db.Column(db.String(128), nullable=False)
    field_of_study = db.Column(db.String(128), nullable=True)
    start_date = db.Column(db.Date, nullable=True)
    end_date = db.Column(db.Date, nullable=True)
    gpa = db.Column(db.String(16), nullable=True)

class CandidateSkill(BaseModel):
    __tablename__ = 'candidate_skills'

    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id', ondelete='CASCADE'), nullable=False, index=True)
    skill_id = db.Column(db.Integer, db.ForeignKey('skills.id', ondelete='SET NULL'), nullable=True, index=True)
    skill_name = db.Column(db.String(64), nullable=False, index=True)
    years_of_experience = db.Column(db.Float, default=1.0)
    proficiency = db.Column(db.String(32), default='INTERMEDIATE') # BEGINNER, INTERMEDIATE, EXPERT
    confidence_score = db.Column(db.Float, default=1.0) # AI extraction confidence 0.0 - 1.0
    is_verified = db.Column(db.Boolean, default=False)

    skill = db.relationship('Skill', foreign_keys=[skill_id])

class CandidateCertification(BaseModel):
    __tablename__ = 'candidate_certifications'

    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id', ondelete='CASCADE'), nullable=False, index=True)
    name = db.Column(db.String(128), nullable=False)
    issuing_organization = db.Column(db.String(128), nullable=False)
    issue_date = db.Column(db.Date, nullable=True)
    expiration_date = db.Column(db.Date, nullable=True)
    credential_id = db.Column(db.String(128), nullable=True)
    credential_url = db.Column(db.String(512), nullable=True)

class CandidateLanguage(BaseModel):
    __tablename__ = 'candidate_languages'

    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id', ondelete='CASCADE'), nullable=False, index=True)
    language = db.Column(db.String(64), nullable=False)
    proficiency = db.Column(db.String(32), default='PROFICIENT') # NATIVE, FLUENT, PROFICIENT, BASIC

class CandidateProject(BaseModel):
    __tablename__ = 'candidate_projects'

    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id', ondelete='CASCADE'), nullable=False, index=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=True)
    technologies = db.Column(db.JSON, default=list) # ["Python", "Flask", "PostgreSQL"]
    project_url = db.Column(db.String(512), nullable=True)

class CandidateTag(BaseModel):
    __tablename__ = 'candidate_tags'

    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id', ondelete='CASCADE'), nullable=False, index=True)
    tag = db.Column(db.String(64), nullable=False, index=True)
    created_by_user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'), nullable=True)

class CandidateNote(BaseModel):
    __tablename__ = 'candidate_notes'

    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id', ondelete='CASCADE'), nullable=False, index=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'), nullable=False)
    note = db.Column(db.Text, nullable=False)
    is_private = db.Column(db.Boolean, default=False)

    author = db.relationship('User')

class CandidateActivity(BaseModel):
    __tablename__ = 'candidate_activities'

    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id', ondelete='CASCADE'), nullable=False, index=True)
    actor_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'), nullable=True)
    activity_type = db.Column(db.String(64), nullable=False) # PROFILE_CREATED, RESUME_UPLOADED, STAGE_CHANGED, INTERVIEW_SCHEDULED, SCORE_RECALCULATED
    description = db.Column(db.String(255), nullable=False)
    metadata_json = db.Column(db.JSON, nullable=True)
