from marshmallow import Schema, fields, validate

class WorkflowRuleSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=3, max=128))
    is_active = fields.Boolean(missing=True)
    trigger_event = fields.String(required=True)
    conditions = fields.List(fields.Dict(), required=True) # [{"field": "score", "operator": ">=", "value": 85}]
    actions = fields.List(fields.Dict(), required=True) # [{"type": "move_stage", "target": "Shortlisted"}]
    created_at = fields.DateTime(dump_only=True)

class WorkflowExecutionSchema(Schema):
    id = fields.Integer(dump_only=True)
    rule_id = fields.Integer()
    target_entity_id = fields.Integer()
    target_entity_type = fields.String()
    status = fields.String()
    error_message = fields.String(allow_none=True)
    created_at = fields.DateTime()
