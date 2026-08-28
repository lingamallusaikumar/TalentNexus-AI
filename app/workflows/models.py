from app.common.models import BaseModel
from app.extensions import db

class WorkflowRule(BaseModel):
    __tablename__ = 'workflow_rules'

    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id'), nullable=False)
    
    name = db.Column(db.String(128), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    
    trigger_event = db.Column(db.String(64), nullable=False) # e.g., 'candidate.match.completed', 'application.stage.changed'
    
    # JSON structure storing criteria e.g., {"field": "score", "operator": ">=", "value": 85}
    conditions = db.Column(db.JSON, nullable=False)
    
    # JSON structure storing action e.g., {"type": "move_stage", "target": "Shortlisted"}
    actions = db.Column(db.JSON, nullable=False)
    
    organization = db.relationship('Organization', backref=db.backref('workflow_rules', cascade="all, delete-orphan"))

class WorkflowExecution(BaseModel):
    __tablename__ = 'workflow_executions'
    
    rule_id = db.Column(db.Integer, db.ForeignKey('workflow_rules.id'), nullable=False)
    target_entity_id = db.Column(db.Integer, nullable=False) # Could be Candidate ID, Application ID
    target_entity_type = db.Column(db.String(64), nullable=False)
    
    status = db.Column(db.String(32), default='Success') # Success, Failed
    error_message = db.Column(db.Text, nullable=True)
    
    rule = db.relationship('WorkflowRule', backref=db.backref('executions', cascade="all, delete-orphan"))
