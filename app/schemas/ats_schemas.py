from marshmallow import Schema, fields, validate

class ApplicationCreateSchema(Schema):
    job_id = fields.Integer(required=True)
    source = fields.String(validate=validate.OneOf([
        'CAREERS_PORTAL', 'LINKEDIN', 'REFERRAL', 'AGENCY', 'SOURCED', 'DIRECT'
    ]), missing='CAREERS_PORTAL')

class ApplicationStageMoveSchema(Schema):
    target_stage = fields.String(required=True)
    notes = fields.String(allow_none=True)

class ApplicationHistorySchema(Schema):
    id = fields.Integer()
    from_stage = fields.String()
    to_stage = fields.String()
    notes = fields.String()
    is_automated = fields.Boolean()
    created_at = fields.DateTime()

class ApplicationResponseSchema(Schema):
    id = fields.Integer()
    candidate_id = fields.Integer()
    job_id = fields.Integer()
    candidate_name = fields.Method("get_candidate_name")
    job_title = fields.Method("get_job_title")
    current_stage = fields.String()
    status = fields.String()
    source = fields.String()
    is_sla_breached = fields.Boolean()
    sla_deadline = fields.DateTime()
    applied_at = fields.DateTime()
    history = fields.Nested(ApplicationHistorySchema, many=True)

    def get_candidate_name(self, obj):
        if obj.candidate:
            return f"{obj.candidate.first_name or ''} {obj.candidate.last_name or ''}".strip()
        return "Unknown"

    def get_job_title(self, obj):
        return obj.job.title if obj.job else "Unknown"
