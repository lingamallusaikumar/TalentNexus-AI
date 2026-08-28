from datetime import datetime
from app.common.models import BaseModel
from app.extensions import db

class MLModelRegistry(BaseModel):
    __tablename__ = 'ml_model_registries'

    model_name = db.Column(db.String(128), nullable=False, index=True) # e.g. "CandidateMatchScorer", "ResumeSectionNER"
    model_type = db.Column(db.String(64), nullable=False) # EMBEDDING, CLASSIFIER, NER, REGRESSION
    current_production_version = db.Column(db.String(32), default='v1.0.0')
    description = db.Column(db.Text, nullable=True)

    versions = db.relationship('MLModelVersion', backref='model_registry', cascade="all, delete-orphan")

class MLModelVersion(BaseModel):
    __tablename__ = 'ml_model_versions'

    registry_id = db.Column(db.Integer, db.ForeignKey('ml_model_registries.id', ondelete='CASCADE'), nullable=False, index=True)
    version = db.Column(db.String(32), nullable=False) # v1.0.0
    artifact_path = db.Column(db.String(512), nullable=False) # S3 or local path
    parameters = db.Column(db.JSON, default=dict)
    
    # Evaluation Metrics
    accuracy = db.Column(db.Float, nullable=True)
    f1_score = db.Column(db.Float, nullable=True)
    latency_p95_ms = db.Column(db.Float, nullable=True)
    
    status = db.Column(db.String(32), default='STAGING') # STAGING, PRODUCTION, ARCHIVED, RETIRED
    deployed_at = db.Column(db.DateTime, nullable=True)

class ModelInferenceLog(BaseModel):
    __tablename__ = 'model_inference_logs'

    model_version_id = db.Column(db.Integer, db.ForeignKey('ml_model_versions.id', ondelete='CASCADE'), nullable=True, index=True)
    model_name = db.Column(db.String(128), nullable=False, index=True)
    latency_ms = db.Column(db.Float, nullable=False)
    input_token_count = db.Column(db.Integer, default=0)
    prediction_score = db.Column(db.Float, nullable=True)
    error = db.Column(db.String(255), nullable=True)
