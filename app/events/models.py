from app.common.models import BaseModel
from app.extensions import db

class EventLog(BaseModel):
    __tablename__ = 'event_logs'

    event_name = db.Column(db.String(128), nullable=False, index=True)
    entity_type = db.Column(db.String(64), nullable=False, index=True)
    entity_id = db.Column(db.Integer, nullable=False, index=True)
    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id', ondelete='CASCADE'), nullable=True, index=True)
    actor_user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'), nullable=True)
    
    payload = db.Column(db.JSON, nullable=True)
    status = db.Column(db.String(32), default='PUBLISHED', index=True) # PUBLISHED, PROCESSED, FAILED
    error_message = db.Column(db.Text, nullable=True)

    organization = db.relationship('Organization', foreign_keys=[organization_id])
    actor = db.relationship('User', foreign_keys=[actor_user_id])
