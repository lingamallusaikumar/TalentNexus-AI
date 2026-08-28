from app.common.models import BaseModel
from app.extensions import db

class Interview(BaseModel):
    __tablename__ = 'interviews'

    application_id = db.Column(db.Integer, db.ForeignKey('applications.id'), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    round_number = db.Column(db.Integer, default=1)
    
    scheduled_at = db.Column(db.DateTime, nullable=False)
    duration_minutes = db.Column(db.Integer, default=60)
    
    location = db.Column(db.String(255), nullable=True) # Zoom link, physical room, etc.
    status = db.Column(db.String(32), default='Scheduled') # Scheduled, Completed, Cancelled
    
    application = db.relationship('Application', backref=db.backref('interviews', cascade="all, delete-orphan"))

class Interviewer(BaseModel):
    __tablename__ = 'interviewers'
    
    interview_id = db.Column(db.Integer, db.ForeignKey('interviews.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Relationship
    interview = db.relationship('Interview', backref=db.backref('interviewers', cascade="all, delete-orphan"))
    user = db.relationship('User')

class InterviewFeedback(BaseModel):
    __tablename__ = 'interview_feedback'
    
    interview_id = db.Column(db.Integer, db.ForeignKey('interviews.id'), nullable=False)
    interviewer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    rating = db.Column(db.Integer, nullable=True) # 1-5 scale
    notes = db.Column(db.Text, nullable=False)
    recommendation = db.Column(db.String(32), nullable=True) # Strong Hire, Hire, Weak No, Strong No
    
    interview = db.relationship('Interview', backref=db.backref('feedback', cascade="all, delete-orphan"))
    interviewer = db.relationship('User')
