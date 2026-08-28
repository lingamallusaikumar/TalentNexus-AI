from app.common.models import BaseModel, SoftDeleteMixin
from app.extensions import db

class Job(BaseModel, SoftDeleteMixin):
    __tablename__ = 'jobs'

    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id', ondelete='CASCADE'), nullable=False, index=True)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id', ondelete='SET NULL'), nullable=True, index=True)
    hiring_manager_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'), nullable=True, index=True)
    created_by_user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'), nullable=True)
    
    title = db.Column(db.String(128), nullable=False, index=True)
    slug = db.Column(db.String(160), nullable=True, index=True)
    code = db.Column(db.String(32), nullable=True) # e.g. ENG-2026-004
    location = db.Column(db.String(128), nullable=True, index=True)
    is_remote = db.Column(db.Boolean, default=False, index=True)
    remote_type = db.Column(db.String(32), default='ONSITE') # ONSITE, HYBRID, FULLY_REMOTE
    employment_type = db.Column(db.String(64), default='FULL_TIME') # FULL_TIME, PART_TIME, CONTRACT, INTERNSHIP
    
    description = db.Column(db.Text, nullable=False)
    raw_requirements = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(32), default='DRAFT', index=True) # DRAFT, PENDING_APPROVAL, PUBLISHED, PAUSED, CLOSED, ARCHIVED
    
    # Compensation
    salary_min = db.Column(db.Integer, nullable=True)
    salary_max = db.Column(db.Integer, nullable=True)
    salary_currency = db.Column(db.String(3), default='USD')
    is_salary_visible = db.Column(db.Boolean, default=True)
    
    # AI Job Intelligence Scores
    description_quality_score = db.Column(db.Float, default=0.0) # 0 to 100
    inclusive_language_score = db.Column(db.Float, default=100.0) # 0 to 100
    jd_analysis = db.Column(db.JSON, nullable=True)
    job_embedding = db.Column(db.JSON, nullable=True) # Vector representation for vector search
    
    expires_at = db.Column(db.DateTime, nullable=True)

    # Relationships
    requirements = db.relationship('JobRequirement', backref='job', cascade="all, delete-orphan")
    activities = db.relationship('JobActivity', backref='job', cascade="all, delete-orphan", order_by="desc(JobActivity.created_at)")
    approvals = db.relationship('JobApproval', backref='job', cascade="all, delete-orphan")

class JobRequirement(BaseModel):
    __tablename__ = 'job_requirements'
    
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id', ondelete='CASCADE'), nullable=False, index=True)
    skill_id = db.Column(db.Integer, db.ForeignKey('skills.id', ondelete='SET NULL'), nullable=True, index=True)
    
    skill_name = db.Column(db.String(64), nullable=False, index=True)
    is_required = db.Column(db.Boolean, default=True, nullable=False) # True = Mandatory, False = Preferred / Nice to have
    min_years_experience = db.Column(db.Float, default=1.0)
    weight = db.Column(db.Float, default=1.0) # Relative matching weight

class JobTemplate(BaseModel):
    __tablename__ = 'job_templates'

    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id', ondelete='CASCADE'), nullable=False, index=True)
    name = db.Column(db.String(128), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    department = db.Column(db.String(128), nullable=True)
    description = db.Column(db.Text, nullable=False)
    default_requirements = db.Column(db.JSON, default=list) # [{"skill_name": "Python", "is_required": True, "years": 3}]

class JobApproval(BaseModel):
    __tablename__ = 'job_approvals'

    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id', ondelete='CASCADE'), nullable=False, index=True)
    approver_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    status = db.Column(db.String(32), default='PENDING') # PENDING, APPROVED, REJECTED
    comments = db.Column(db.Text, nullable=True)
    actioned_at = db.Column(db.DateTime, nullable=True)

class JobActivity(BaseModel):
    __tablename__ = 'job_activities'

    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id', ondelete='CASCADE'), nullable=False, index=True)
    actor_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'), nullable=True)
    action = db.Column(db.String(64), nullable=False) # CREATED, PUBLISHED, UPDATED, CLONED, CLOSED
    details = db.Column(db.JSON, nullable=True)
