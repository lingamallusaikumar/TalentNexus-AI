from app.common.models import BaseModel
from app.extensions import db

class Resume(BaseModel):
    __tablename__ = 'resumes'

    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id'), nullable=False)
    file_name = db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.String(512), nullable=False) # S3 or local path
    file_type = db.Column(db.String(32), nullable=False) # pdf, docx, etc.
    file_size_bytes = db.Column(db.Integer, nullable=True)
    
    raw_text = db.Column(db.Text, nullable=True) # Extracted text
    
    is_parsed = db.Column(db.Boolean, default=False)
    parsing_status = db.Column(db.String(32), default='Pending') # Pending, Processing, Completed, Failed
    parsing_error = db.Column(db.Text, nullable=True)
    
    candidate = db.relationship('Candidate', backref=db.backref('resumes', cascade="all, delete-orphan"))

class ResumeProcessingJob(BaseModel):
    __tablename__ = 'resume_processing_jobs'
    
    resume_id = db.Column(db.Integer, db.ForeignKey('resumes.id'), nullable=False)
    celery_task_id = db.Column(db.String(128), nullable=True)
    status = db.Column(db.String(32), default='Queued')
    started_at = db.Column(db.DateTime, nullable=True)
    completed_at = db.Column(db.DateTime, nullable=True)
    
    resume = db.relationship('Resume', backref=db.backref('processing_jobs', cascade="all, delete-orphan"))
