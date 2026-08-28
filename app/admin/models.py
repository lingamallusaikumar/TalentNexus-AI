from app.common.models import BaseModel
from app.extensions import db

class FeatureFlag(BaseModel):
    __tablename__ = 'feature_flags'

    name = db.Column(db.String(64), unique=True, nullable=False, index=True)
    description = db.Column(db.String(255), nullable=True)
    is_enabled_globally = db.Column(db.Boolean, default=False)
    organization_overrides = db.Column(db.JSON, default=dict) # {"org_id_1": True, "org_id_2": False}

class SystemConfig(BaseModel):
    __tablename__ = 'system_configs'

    key = db.Column(db.String(64), unique=True, nullable=False, index=True)
    value = db.Column(db.JSON, nullable=False)
    description = db.Column(db.String(255), nullable=True)
