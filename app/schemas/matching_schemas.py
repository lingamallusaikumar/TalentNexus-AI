from marshmallow import Schema, fields, validate

class ScoringProfileSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=2, max=128))
    is_default = fields.Boolean(missing=False)
    weight_required_skills = fields.Float(missing=0.30)
    weight_semantic_similarity = fields.Float(missing=0.20)
    weight_experience = fields.Float(missing=0.15)
    weight_projects = fields.Float(missing=0.10)
    weight_education = fields.Float(missing=0.10)
    weight_certifications = fields.Float(missing=0.05)
    weight_location = fields.Float(missing=0.05)
    weight_preferences = fields.Float(missing=0.05)

class CandidateMatchRequestSchema(Schema):
    candidate_id = fields.Integer(required=True)
    job_id = fields.Integer(required=True)
    scoring_profile_id = fields.Integer(allow_none=True)

class CandidateMatchResponseSchema(Schema):
    id = fields.Integer()
    candidate_id = fields.Integer()
    job_id = fields.Integer()
    overall_score = fields.Float()
    rank_position = fields.Integer()
    recommendation = fields.String()
    score_skills = fields.Float()
    score_semantic = fields.Float()
    score_experience = fields.Float()
    score_projects = fields.Float()
    score_education = fields.Float()
    score_certifications = fields.Float()
    score_location = fields.Float()
    score_preferences = fields.Float()
    explanation = fields.Dict()
    is_overridden = fields.Boolean()
    human_decision = fields.String(allow_none=True)
    override_reason = fields.String(allow_none=True)
    created_at = fields.DateTime()

class RecruiterOverrideSchema(Schema):
    candidate_id = fields.Integer(required=True)
    job_id = fields.Integer(required=True)
    human_decision = fields.String(required=True, validate=validate.OneOf(['SHORTLIST', 'REVIEW', 'REJECT', 'HIRE']))
    override_reason = fields.String(required=True, validate=validate.Length(min=5, max=500))
