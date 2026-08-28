from app.common.models import BaseModel
from app.extensions import db

class Job(BaseModel):
    __tablename__ = 'jobs'

    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id'), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    department = db.Column(db.String(128), nullable=True)
    location = db.Column(db.String(128), nullable=True)
    is_remote = db.Column(db.Boolean, default=False)
    employment_type = db.Column(db.String(64), nullable=True) # Full-time, Part-time, Contract
    
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(32), default='Draft') # Draft, Published, Closed
    
    salary_min = db.Column(db.Integer, nullable=True)
    salary_max = db.Column(db.Integer, nullable=True)
    salary_currency = db.Column(db.String(3), default='USD')
    
    # Relationships
    requirements = db.relationship('JobRequirement', backref='job', cascade="all, delete-orphan")

class JobRequirement(BaseModel):
    __tablename__ = 'job_requirements'
    
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)
    # Extracted by AI or manually added
    skill_name = db.Column(db.String(64), nullable=False)
    is_required = db.Column(db.Boolean, default=True)
    min_years_experience = db.Column(db.Float, nullable=True)
    weight = db.Column(db.Float, default=1.0) # Importance for matching engine
