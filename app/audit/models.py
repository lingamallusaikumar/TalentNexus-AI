from app.common.models import BaseModel
from app.extensions import db

class AuditLog(BaseModel):
    __tablename__ = 'audit_logs'

    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id', ondelete='CASCADE'), nullable=True, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'), nullable=True, index=True)
    
    action = db.Column(db.String(64), nullable=False, index=True) # CREATE, UPDATE, DELETE, LOGIN, EXPORT, OVERRIDE_AI
    resource_type = db.Column(db.String(64), nullable=False, index=True)
    resource_id = db.Column(db.Integer, nullable=True, index=True)
    
    changes = db.Column(db.JSON, nullable=True) # {"before": {...}, "after": {...}}
    ip_address = db.Column(db.String(45), nullable=True)
    user_agent = db.Column(db.String(255), nullable=True)

    user = db.relationship('User', foreign_keys=[user_id])
    organization = db.relationship('Organization', foreign_keys=[organization_id])

class SecurityLog(BaseModel):
    __tablename__ = 'security_logs'

    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id', ondelete='CASCADE'), nullable=True, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'), nullable=True, index=True)
    
    event_type = db.Column(db.String(64), nullable=False, index=True) # LOGIN_FAILED, 2FA_FAILED, TOKEN_REVOKED, PERMISSION_DENIED, RATE_LIMIT_EXCEEDED
    severity = db.Column(db.String(16), default='INFO', index=True) # INFO, WARNING, CRITICAL
    ip_address = db.Column(db.String(45), nullable=True)
    user_agent = db.Column(db.String(255), nullable=True)
    details = db.Column(db.JSON, nullable=True)
