from datetime import datetime
from app.common.models import BaseModel
from app.extensions import db

class Assessment(BaseModel):
    __tablename__ = 'assessments'

    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id', ondelete='CASCADE'), nullable=False, index=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=True)
    time_limit_minutes = db.Column(db.Integer, default=45)
    passing_score_percentage = db.Column(db.Float, default=70.0)
    is_active = db.Column(db.Boolean, default=True)

    questions = db.relationship('AssessmentQuestion', backref='assessment', cascade="all, delete-orphan", order_by="AssessmentQuestion.order_num")
    attempts = db.relationship('AssessmentAttempt', backref='assessment', cascade="all, delete-orphan")

class AssessmentQuestion(BaseModel):
    __tablename__ = 'assessment_questions'

    assessment_id = db.Column(db.Integer, db.ForeignKey('assessments.id', ondelete='CASCADE'), nullable=False, index=True)
    question_text = db.Column(db.Text, nullable=False)
    question_type = db.Column(db.String(32), default='MCQ') # MCQ, CODING, ESSAY, MULTI_SELECT
    points = db.Column(db.Integer, default=10)
    order_num = db.Column(db.Integer, default=1)
    
    # Options format for MCQ: [{"id": 1, "text": "Option A"}, {"id": 2, "text": "Option B"}]
    options = db.Column(db.JSON, default=list)
    correct_answer = db.Column(db.JSON, nullable=False) # e.g. {"answer": 2} or {"tests": [...]}
    explanation = db.Column(db.Text, nullable=True)

class AssessmentAttempt(BaseModel):
    __tablename__ = 'assessment_attempts'

    assessment_id = db.Column(db.Integer, db.ForeignKey('assessments.id', ondelete='CASCADE'), nullable=False, index=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id', ondelete='CASCADE'), nullable=False, index=True)
    application_id = db.Column(db.Integer, db.ForeignKey('applications.id', ondelete='SET NULL'), nullable=True, index=True)
    
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(32), default='IN_PROGRESS') # IN_PROGRESS, COMPLETED, EXPIRED, EVALUATED
    
    score_earned = db.Column(db.Float, default=0.0)
    total_possible_score = db.Column(db.Float, default=100.0)
    percentage_score = db.Column(db.Float, default=0.0)
    is_passed = db.Column(db.Boolean, default=False)
    
    responses = db.Column(db.JSON, default=dict) # {"question_id": selected_answer}
    evaluations = db.Column(db.JSON, default=dict) # detailed question-by-question breakdown
    
    candidate = db.relationship('Candidate', foreign_keys=[candidate_id])
    application = db.relationship('Application', foreign_keys=[application_id])
