from datetime import datetime, timedelta
from app.common.models import BaseModel, SoftDeleteMixin
from app.extensions import db

# Default Stage Names
STAGE_APPLIED = 'Applied'
STAGE_AI_SCREENING = 'AI Screening'
STAGE_RECRUITER_REVIEW = 'Recruiter Review'
STAGE_SHORTLISTED = 'Shortlisted'
STAGE_ASSESSMENT = 'Assessment'
STAGE_INTERVIEW = 'Interview'
STAGE_OFFER = 'Offer'
STAGE_HIRED = 'Hired'
STAGE_REJECTED = 'Rejected'

class RecruitmentPipeline(BaseModel):
    __tablename__ = 'recruitment_pipelines'

    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id', ondelete='CASCADE'), nullable=False, index=True)
    name = db.Column(db.String(128), nullable=False) # e.g. "Standard Engineering", "Executive Pipeline"
    is_default = db.Column(db.Boolean, default=False)

    stages = db.relationship('PipelineStage', backref='pipeline', cascade="all, delete-orphan", order_by="PipelineStage.position")

class PipelineStage(BaseModel):
    __tablename__ = 'pipeline_stages'

    pipeline_id = db.Column(db.Integer, db.ForeignKey('recruitment_pipelines.id', ondelete='CASCADE'), nullable=False, index=True)
    name = db.Column(db.String(64), nullable=False)
    position = db.Column(db.Integer, default=1)
    stage_type = db.Column(db.String(32), default='CUSTOM') # APPLIED, SCREENING, SHORTLIST, ASSESSMENT, INTERVIEW, OFFER, HIRED, REJECTED
    sla_hours = db.Column(db.Integer, default=48) # SLA limit in hours for candidates staying in this stage
    auto_trigger_assessment_id = db.Column(db.Integer, nullable=True) # Optional auto-assessment trigger

class Application(BaseModel, SoftDeleteMixin):
    __tablename__ = 'applications'

    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id', ondelete='CASCADE'), nullable=False, index=True)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id', ondelete='CASCADE'), nullable=False, index=True)
    current_stage = db.Column(db.String(64), default=STAGE_APPLIED, nullable=False, index=True)
    status = db.Column(db.String(32), default='ACTIVE', index=True) # ACTIVE, REJECTED, HIRED, WITHDRAWN
    
    source = db.Column(db.String(64), default='CAREERS_PORTAL') # CAREERS_PORTAL, LINKEDIN, REFERRAL, AGENCY, SOURCED
    applied_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    stage_entered_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    # SLA Tracking
    is_sla_breached = db.Column(db.Boolean, default=False, index=True)
    sla_deadline = db.Column(db.DateTime, default=lambda: datetime.utcnow() + timedelta(hours=48))
    
    # Rejection info
    rejection_reason = db.Column(db.String(128), nullable=True)
    rejection_notes = db.Column(db.Text, nullable=True)
    rejected_at = db.Column(db.DateTime, nullable=True)
    
    # Relationships
    candidate = db.relationship('Candidate', backref=db.backref('applications', cascade="all, delete-orphan"))
    job = db.relationship('Job', backref=db.backref('applications', cascade="all, delete-orphan"))
    history = db.relationship('ApplicationHistory', backref='application', cascade="all, delete-orphan", order_by="desc(ApplicationHistory.created_at)")
    interviews = db.relationship('Interview', backref='application', cascade="all, delete-orphan")

    __table_args__ = (
        db.UniqueConstraint('candidate_id', 'job_id', name='uq_candidate_job_application'),
    )

class ApplicationHistory(BaseModel):
    __tablename__ = 'application_history'
    
    application_id = db.Column(db.Integer, db.ForeignKey('applications.id', ondelete='CASCADE'), nullable=False, index=True)
    moved_by_user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'), nullable=True)
    
    from_stage = db.Column(db.String(64), nullable=True)
    to_stage = db.Column(db.String(64), nullable=False)
    notes = db.Column(db.Text, nullable=True)
    is_automated = db.Column(db.Boolean, default=False)
    
    user = db.relationship('User', foreign_keys=[moved_by_user_id])
