from datetime import datetime
from app.common.models import BaseModel
from app.extensions import db

class Interview(BaseModel):
    __tablename__ = 'interviews'

    application_id = db.Column(db.Integer, db.ForeignKey('applications.id', ondelete='CASCADE'), nullable=False, index=True)
    title = db.Column(db.String(128), nullable=False) # e.g. "Round 1: System Design & Architecture"
    round_number = db.Column(db.Integer, default=1)
    interview_type = db.Column(db.String(64), default='TECHNICAL') # BEHAVIORAL, TECHNICAL, SYSTEM_DESIGN, HR_SCREEN, FINAL
    
    scheduled_at = db.Column(db.DateTime, nullable=False, index=True)
    duration_minutes = db.Column(db.Integer, default=60)
    
    meeting_link = db.Column(db.String(512), nullable=True)
    location = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(32), default='SCHEDULED', index=True) # SCHEDULED, IN_PROGRESS, COMPLETED, CANCELLED, NO_SHOW
    
    interviewer_notes = db.Column(db.Text, nullable=True)
    final_recommendation = db.Column(db.String(32), nullable=True) # STRONG_HIRE, HIRE, LEANING_HIRE, LEANING_NO, STRONG_NO
    
    # Relationships
    panel_members = db.relationship('Interviewer', backref='interview', cascade="all, delete-orphan")
    feedbacks = db.relationship('InterviewFeedback', backref='interview', cascade="all, delete-orphan")

class Interviewer(BaseModel):
    __tablename__ = 'interviewers'
    
    interview_id = db.Column(db.Integer, db.ForeignKey('interviews.id', ondelete='CASCADE'), nullable=False, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    is_lead = db.Column(db.Boolean, default=False)
    
    user = db.relationship('User', foreign_keys=[user_id])

class InterviewScorecardTemplate(BaseModel):
    __tablename__ = 'interview_scorecard_templates'

    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id', ondelete='CASCADE'), nullable=False, index=True)
    name = db.Column(db.String(128), nullable=False)
    criteria = db.Column(db.JSON, default=list) # [{"name": "Coding Skill", "weight": 0.4}, {"name": "Communication", "weight": 0.3}]

class InterviewFeedback(BaseModel):
    __tablename__ = 'interview_feedback'
    
    interview_id = db.Column(db.Integer, db.ForeignKey('interviews.id', ondelete='CASCADE'), nullable=False, index=True)
    interviewer_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    
    overall_rating = db.Column(db.Integer, nullable=False) # 1 to 5 scale
    criteria_ratings = db.Column(db.JSON, default=dict) # {"Problem Solving": 5, "Communication": 4, "System Design": 4}
    
    strengths = db.Column(db.Text, nullable=True)
    areas_for_improvement = db.Column(db.Text, nullable=True)
    notes = db.Column(db.Text, nullable=False)
    recommendation = db.Column(db.String(32), nullable=False) # STRONG_HIRE, HIRE, LEANING_HIRE, LEANING_NO, STRONG_NO
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    interviewer = db.relationship('User', foreign_keys=[interviewer_id])
