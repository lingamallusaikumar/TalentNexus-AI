from datetime import datetime
from app.common.models import BaseModel
from app.extensions import db

class Notification(BaseModel):
    __tablename__ = 'notifications'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id', ondelete='CASCADE'), nullable=True, index=True)
    
    title = db.Column(db.String(128), nullable=False)
    message = db.Column(db.Text, nullable=False)
    notification_type = db.Column(db.String(64), default='INFO') # NEW_APPLICATION, RESUME_PARSED, SCORE_UPDATED, INTERVIEW_SCHEDULED, ASSESSMENT_COMPLETED
    
    link_url = db.Column(db.String(255), nullable=True)
    is_read = db.Column(db.Boolean, default=False, nullable=False, index=True)
    read_at = db.Column(db.DateTime, nullable=True)

    user = db.relationship('User', foreign_keys=[user_id])

class NotificationPreference(BaseModel):
    __tablename__ = 'notification_preferences'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, unique=True, index=True)
    email_on_new_application = db.Column(db.Boolean, default=True)
    email_on_interview_scheduled = db.Column(db.Boolean, default=True)
    email_on_assessment_completed = db.Column(db.Boolean, default=True)
    in_app_sound_enabled = db.Column(db.Boolean, default=True)
