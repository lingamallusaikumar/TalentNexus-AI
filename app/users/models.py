from datetime import datetime, timedelta
import secrets
from app.common.models import BaseModel, SoftDeleteMixin
from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

# Standard Permission Codes
PERM_VIEW_DASHBOARD = 'dashboard.view'
PERM_MANAGE_ORGANIZATION = 'org.manage'
PERM_MANAGE_USERS = 'users.manage'
PERM_CREATE_JOB = 'jobs.create'
PERM_EDIT_JOB = 'jobs.edit'
PERM_DELETE_JOB = 'jobs.delete'
PERM_VIEW_CANDIDATES = 'candidates.view'
PERM_SCREEN_RESUME = 'resumes.screen'
PERM_OVERRIDE_AI = 'ai.override'
PERM_SCHEDULE_INTERVIEW = 'interviews.schedule'
PERM_SUBMIT_FEEDBACK = 'interviews.feedback'
PERM_MANAGE_WORKFLOWS = 'workflows.manage'
PERM_EXPORT_ANALYTICS = 'analytics.export'

class Permission(BaseModel):
    __tablename__ = 'permissions'

    code = db.Column(db.String(64), unique=True, nullable=False, index=True)
    name = db.Column(db.String(128), nullable=False)
    category = db.Column(db.String(64), nullable=False) # e.g. JOBS, CANDIDATES, ADMIN, AI
    description = db.Column(db.String(255), nullable=True)

class RolePermission(BaseModel):
    __tablename__ = 'role_permissions'

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id', ondelete='CASCADE'), nullable=False, index=True)
    permission_id = db.Column(db.Integer, db.ForeignKey('permissions.id', ondelete='CASCADE'), nullable=False, index=True)

    permission = db.relationship('Permission')

class Role(BaseModel):
    __tablename__ = 'roles'
    
    name = db.Column(db.String(64), unique=True, nullable=False, index=True)
    code = db.Column(db.String(32), unique=True, nullable=False, index=True) # SUPER_ADMIN, ORG_ADMIN, HR_MANAGER, RECRUITER, HIRING_MANAGER, INTERVIEWER, CANDIDATE
    description = db.Column(db.String(255), nullable=True)
    is_system = db.Column(db.Boolean, default=True) # True for immutable built-in roles
    
    role_permissions = db.relationship('RolePermission', backref='role', cascade="all, delete-orphan")

    def has_permission(self, permission_code: str) -> bool:
        if self.code == 'SUPER_ADMIN':
            return True
        return any(rp.permission.code == permission_code for rp in self.role_permissions if rp.permission)

class User(BaseModel, SoftDeleteMixin):
    __tablename__ = 'users'

    email = db.Column(db.String(128), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.String(32), nullable=True)
    avatar_url = db.Column(db.String(512), nullable=True)
    
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    is_verified = db.Column(db.Boolean, default=False, nullable=False)
    
    # 2FA
    two_factor_enabled = db.Column(db.Boolean, default=False, nullable=False)
    two_factor_secret = db.Column(db.String(64), nullable=True)
    
    # Active tenant context
    current_organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id', ondelete='SET NULL'), nullable=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id', ondelete='RESTRICT'), nullable=False)
    
    # Security tracking
    last_login_at = db.Column(db.DateTime, nullable=True)
    failed_login_attempts = db.Column(db.Integer, default=0, nullable=False)
    lockout_until = db.Column(db.DateTime, nullable=True)

    role = db.relationship('Role', foreign_keys=[role_id])
    current_organization = db.relationship('Organization', foreign_keys=[current_organization_id])
    sessions = db.relationship('UserSession', backref='user', cascade="all, delete-orphan")
    login_history = db.relationship('LoginHistory', backref='user', cascade="all, delete-orphan")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    @property
    def password(self):
        raise AttributeError('password is not readable')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def can(self, permission_code: str) -> bool:
        if self.role:
            return self.role.has_permission(permission_code)
        return False

    def is_locked(self) -> bool:
        if self.lockout_until and self.lockout_until > datetime.utcnow():
            return True
        return False

class UserSession(BaseModel):
    __tablename__ = 'user_sessions'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    token_jti = db.Column(db.String(128), unique=True, nullable=False, index=True)
    ip_address = db.Column(db.String(45), nullable=True)
    user_agent = db.Column(db.String(255), nullable=True)
    device_type = db.Column(db.String(64), default='DESKTOP')
    expires_at = db.Column(db.DateTime, nullable=False)
    is_revoked = db.Column(db.Boolean, default=False, nullable=False)

class LoginHistory(BaseModel):
    __tablename__ = 'login_histories'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    ip_address = db.Column(db.String(45), nullable=True)
    user_agent = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(32), default='SUCCESS') # SUCCESS, FAILED, LOCKED, 2FA_REQUIRED
    failure_reason = db.Column(db.String(128), nullable=True)

class PasswordResetToken(BaseModel):
    __tablename__ = 'password_reset_tokens'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    token = db.Column(db.String(128), unique=True, nullable=False, default=lambda: secrets.token_urlsafe(32), index=True)
    expires_at = db.Column(db.DateTime, default=lambda: datetime.utcnow() + timedelta(hours=2), nullable=False)
    used_at = db.Column(db.DateTime, nullable=True)
