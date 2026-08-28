from datetime import datetime, timedelta
import secrets
from app.common.models import BaseModel, SoftDeleteMixin
from app.extensions import db

class Organization(BaseModel, SoftDeleteMixin):
    __tablename__ = 'organizations'

    name = db.Column(db.String(128), nullable=False, index=True)
    slug = db.Column(db.String(128), unique=True, nullable=True, index=True)
    domain = db.Column(db.String(128), unique=True, nullable=True, index=True)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    
    # Custom branding and tenant configuration
    branding = db.Column(db.JSON, default=dict) # {"logo_url": "...", "primary_color": "#0F52BA", "company_website": "..."}
    settings = db.Column(db.JSON, default=dict) # {"default_currency": "USD", "scoring_weights": {...}, "sla_days_per_stage": {...}}
    
    # Relationships
    workspaces = db.relationship('Workspace', backref='organization', cascade="all, delete-orphan")
    departments = db.relationship('Department', backref='organization', cascade="all, delete-orphan")
    memberships = db.relationship('OrganizationMembership', backref='organization', cascade="all, delete-orphan")
    invitations = db.relationship('Invitation', backref='organization', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Organization {self.name}>"

class Workspace(BaseModel):
    __tablename__ = 'workspaces'

    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id', ondelete='CASCADE'), nullable=False, index=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    is_active = db.Column(db.Boolean, default=True)

class Department(BaseModel):
    __tablename__ = 'departments'

    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id', ondelete='CASCADE'), nullable=False, index=True)
    name = db.Column(db.String(128), nullable=False)
    code = db.Column(db.String(32), nullable=True)
    
    teams = db.relationship('Team', backref='department', cascade="all, delete-orphan")

class Team(BaseModel):
    __tablename__ = 'teams'

    department_id = db.Column(db.Integer, db.ForeignKey('departments.id', ondelete='CASCADE'), nullable=False, index=True)
    name = db.Column(db.String(128), nullable=False)
    lead_user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'), nullable=True)

class OrganizationMembership(BaseModel):
    __tablename__ = 'organization_memberships'

    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id', ondelete='CASCADE'), nullable=False, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id', ondelete='RESTRICT'), nullable=False, index=True)
    is_active = db.Column(db.Boolean, default=True)
    
    role = db.relationship('Role')
    user = db.relationship('User', backref=db.backref('memberships', cascade="all, delete-orphan"))

    __table_args__ = (
        db.UniqueConstraint('organization_id', 'user_id', name='uq_org_user_membership'),
    )

class Invitation(BaseModel):
    __tablename__ = 'invitations'

    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id', ondelete='CASCADE'), nullable=False, index=True)
    invited_by_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'), nullable=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id', ondelete='RESTRICT'), nullable=False)
    
    email = db.Column(db.String(128), nullable=False, index=True)
    token = db.Column(db.String(128), unique=True, nullable=False, default=lambda: secrets.token_urlsafe(32))
    status = db.Column(db.String(32), default='PENDING') # PENDING, ACCEPTED, EXPIRED, REVOKED
    expires_at = db.Column(db.DateTime, default=lambda: datetime.utcnow() + timedelta(days=7))

    role = db.relationship('Role')
    invited_by = db.relationship('User')
