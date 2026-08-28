from app.common.models import BaseModel
from app.extensions import db

class ScoringProfile(BaseModel):
    __tablename__ = 'scoring_profiles'

    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id', ondelete='CASCADE'), nullable=False, index=True)
    name = db.Column(db.String(128), nullable=False) # e.g. "Engineering Default", "Executive Search", "Strict Skills"
    is_default = db.Column(db.Boolean, default=False)
    
    # Configurable weights (must sum to 1.0)
    weight_required_skills = db.Column(db.Float, default=0.30)
    weight_semantic_similarity = db.Column(db.Float, default=0.20)
    weight_experience = db.Column(db.Float, default=0.15)
    weight_projects = db.Column(db.Float, default=0.10)
    weight_education = db.Column(db.Float, default=0.10)
    weight_certifications = db.Column(db.Float, default=0.05)
    weight_location = db.Column(db.Float, default=0.05)
    weight_preferences = db.Column(db.Float, default=0.05)

class CandidateMatch(BaseModel):
    __tablename__ = 'candidate_matches'

    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id', ondelete='CASCADE'), nullable=False, index=True)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id', ondelete='CASCADE'), nullable=False, index=True)
    scoring_profile_id = db.Column(db.Integer, db.ForeignKey('scoring_profiles.id', ondelete='SET NULL'), nullable=True)
    
    overall_score = db.Column(db.Float, default=0.0, nullable=False, index=True) # 0 to 100
    rank_position = db.Column(db.Integer, nullable=True, index=True)
    
    # Sub-factor Scores (0 to 100)
    score_skills = db.Column(db.Float, default=0.0)
    score_semantic = db.Column(db.Float, default=0.0)
    score_experience = db.Column(db.Float, default=0.0)
    score_projects = db.Column(db.Float, default=0.0)
    score_education = db.Column(db.Float, default=0.0)
    score_certifications = db.Column(db.Float, default=0.0)
    score_location = db.Column(db.Float, default=0.0)
    score_preferences = db.Column(db.Float, default=0.0)
    
    # Explainable AI JSON report
    explanation = db.Column(db.JSON, nullable=True)
    recommendation = db.Column(db.String(32), default='REVIEW') # SHORTLIST, REVIEW, REJECT
    
    # Human Feedback Loop
    is_overridden = db.Column(db.Boolean, default=False)
    human_decision = db.Column(db.String(32), nullable=True) # SHORTLIST, REJECT
    override_reason = db.Column(db.Text, nullable=True)
    overridden_by_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'), nullable=True)
    overridden_at = db.Column(db.DateTime, nullable=True)

    candidate = db.relationship('Candidate', backref='job_matches')
    job = db.relationship('Job', backref='candidate_matches')
    overridden_by = db.relationship('User', foreign_keys=[overridden_by_id])

    __table_args__ = (
        db.UniqueConstraint('candidate_id', 'job_id', name='uq_candidate_job_match'),
    )

class RankingHistory(BaseModel):
    __tablename__ = 'ranking_histories'

    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id', ondelete='CASCADE'), nullable=False, index=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id', ondelete='CASCADE'), nullable=False, index=True)
    previous_rank = db.Column(db.Integer, nullable=True)
    new_rank = db.Column(db.Integer, nullable=False)
    previous_score = db.Column(db.Float, nullable=True)
    new_score = db.Column(db.Float, nullable=False)
    trigger_event = db.Column(db.String(64), default='PROFILE_UPDATE')
