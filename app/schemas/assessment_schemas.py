from marshmallow import Schema, fields, validate

class AssessmentQuestionSchema(Schema):
    id = fields.Integer(dump_only=True)
    question_text = fields.String(required=True)
    question_type = fields.String(validate=validate.OneOf(['MCQ', 'CODING', 'ESSAY', 'MULTI_SELECT']), missing='MCQ')
    points = fields.Integer(missing=10)
    order_num = fields.Integer(missing=1)
    options = fields.List(fields.Dict(), missing=list)
    correct_answer = fields.Dict(required=True, load_only=True)
    explanation = fields.String(allow_none=True)

class AssessmentCreateSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(min=3, max=128))
    description = fields.String(allow_none=True)
    time_limit_minutes = fields.Integer(validate=validate.Range(min=5, max=180), missing=45)
    passing_score_percentage = fields.Float(validate=validate.Range(min=10.0, max=100.0), missing=70.0)
    questions = fields.Nested(AssessmentQuestionSchema, many=True, required=True)

class AssessmentAttemptSubmitSchema(Schema):
    assessment_id = fields.Integer(required=True)
    application_id = fields.Integer(allow_none=True)
    responses = fields.Dict(required=True) # {"question_id": selected_answer}
