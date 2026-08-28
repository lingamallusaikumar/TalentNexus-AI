from app.common.models import BaseModel
from app.extensions import db

class Application(BaseModel):
    __tablename__ = 'applications'

    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)
    
    # Standard ATS Stages: Applied, AI Screening, Recruiter Review, Shortlisted, Assessment, Interview, Offer, Hired, Rejected
    current_stage = db.Column(db.String(64), default='Applied')
    status = db.Column(db.String(32), default='Active') # Active, Withdrawn, Rejected, Hired
    
    rejection_reason = db.Column(db.Text, nullable=True)
    
    candidate = db.relationship('Candidate', backref='applications')
    job = db.relationship('Job', backref='applications')
    
    __table_args__ = (
        db.UniqueConstraint('candidate_id', 'job_id', name='uq_candidate_job_application'),
    )

class ApplicationHistory(BaseModel):
    __tablename__ = 'application_history'
    
    application_id = db.Column(db.Integer, db.ForeignKey('applications.id'), nullable=False)
    moved_by_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True) # None if AI moved it
    
    from_stage = db.Column(db.String(64), nullable=True)
    to_stage = db.Column(db.String(64), nullable=False)
    notes = db.Column(db.Text, nullable=True)
    
    application = db.relationship('Application', backref=db.backref('history', cascade="all, delete-orphan"))
    user = db.relationship('User')
