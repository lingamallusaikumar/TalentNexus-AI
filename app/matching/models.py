from app.common.models import BaseModel
from app.extensions import db

class CandidateMatch(BaseModel):
    __tablename__ = 'candidate_matches'

    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)
    
    score = db.Column(db.Float, nullable=False, default=0.0)
    
    # Store JSON explanation for Explainable AI requirement
    explanation = db.Column(db.JSON, nullable=True)
    
    candidate = db.relationship('Candidate', backref='job_matches')
    job = db.relationship('Job', backref='candidate_matches')

    # Ensure a candidate only has one match record per job
    __table_args__ = (
        db.UniqueConstraint('candidate_id', 'job_id', name='uq_candidate_job_match'),
    )
