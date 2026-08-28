from marshmallow import Schema, fields, validate

class InterviewScheduleSchema(Schema):
    application_id = fields.Integer(required=True)
    title = fields.String(required=True, validate=validate.Length(min=3, max=128))
    round_number = fields.Integer(validate=validate.Range(min=1, max=10), missing=1)
    interview_type = fields.String(validate=validate.OneOf([
        'BEHAVIORAL', 'TECHNICAL', 'SYSTEM_DESIGN', 'HR_SCREEN', 'FINAL'
    ]), missing='TECHNICAL')
    scheduled_at = fields.DateTime(required=True)
    duration_minutes = fields.Integer(validate=validate.Range(min=15, max=240), missing=60)
    meeting_link = fields.Url(allow_none=True)
    location = fields.String(allow_none=True)
    interviewer_ids = fields.List(fields.Integer(), required=True, validate=validate.Length(min=1))

class InterviewFeedbackSubmitSchema(Schema):
    interview_id = fields.Integer(required=True)
    overall_rating = fields.Integer(required=True, validate=validate.Range(min=1, max=5))
    criteria_ratings = fields.Dict(keys=fields.String(), values=fields.Integer(validate=validate.Range(min=1, max=5)), missing=dict)
    strengths = fields.String(allow_none=True)
    areas_for_improvement = fields.String(allow_none=True)
    notes = fields.String(required=True, validate=validate.Length(min=10))
    recommendation = fields.String(required=True, validate=validate.OneOf([
        'STRONG_HIRE', 'HIRE', 'LEANING_HIRE', 'LEANING_NO', 'STRONG_NO'
    ]))

class InterviewResponseSchema(Schema):
    id = fields.Integer()
    application_id = fields.Integer()
    title = fields.String()
    round_number = fields.Integer()
    interview_type = fields.String()
    scheduled_at = fields.DateTime()
    duration_minutes = fields.Integer()
    meeting_link = fields.String()
    status = fields.String()
    final_recommendation = fields.String()
