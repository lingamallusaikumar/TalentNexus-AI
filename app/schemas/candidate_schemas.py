from marshmallow import Schema, fields, validate

class CandidateSkillSchema(Schema):
    id = fields.Integer(dump_only=True)
    skill_name = fields.String(required=True, validate=validate.Length(min=1, max=64))
    years_of_experience = fields.Float(validate=validate.Range(min=0.0, max=50.0), missing=1.0)
    proficiency = fields.String(validate=validate.OneOf(['BEGINNER', 'INTERMEDIATE', 'EXPERT']), missing='INTERMEDIATE')
    confidence_score = fields.Float(dump_only=True)
    is_verified = fields.Boolean(missing=False)

class ExperienceSchema(Schema):
    id = fields.Integer(dump_only=True)
    company = fields.String(required=True, validate=validate.Length(min=1, max=128))
    title = fields.String(required=True, validate=validate.Length(min=1, max=128))
    location = fields.String(validate=validate.Length(max=128), allow_none=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(allow_none=True)
    is_current = fields.Boolean(missing=False)
    description = fields.String(allow_none=True)
    achievements = fields.List(fields.String(), missing=list)

class EducationSchema(Schema):
    id = fields.Integer(dump_only=True)
    institution = fields.String(required=True, validate=validate.Length(min=1, max=128))
    degree = fields.String(required=True, validate=validate.Length(min=1, max=128))
    field_of_study = fields.String(validate=validate.Length(max=128), allow_none=True)
    start_date = fields.Date(allow_none=True)
    end_date = fields.Date(allow_none=True)
    gpa = fields.String(validate=validate.Length(max=16), allow_none=True)

class CandidateCertificationSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=1, max=128))
    issuing_organization = fields.String(required=True, validate=validate.Length(min=1, max=128))
    issue_date = fields.Date(allow_none=True)
    expiration_date = fields.Date(allow_none=True)
    credential_id = fields.String(allow_none=True)
    credential_url = fields.Url(allow_none=True)

class CandidateProjectSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(required=True, validate=validate.Length(min=1, max=128))
    description = fields.String(allow_none=True)
    technologies = fields.List(fields.String(), missing=list)
    project_url = fields.Url(allow_none=True)

class CandidateNoteSchema(Schema):
    id = fields.Integer(dump_only=True)
    author_id = fields.Integer(dump_only=True)
    author_name = fields.Method("get_author_name", dump_only=True)
    note = fields.String(required=True)
    is_private = fields.Boolean(missing=False)
    created_at = fields.DateTime(dump_only=True)

    def get_author_name(self, obj):
        return obj.author.full_name if obj.author else "Recruiter"

class CandidateProfileSchema(Schema):
    id = fields.Integer(dump_only=True)
    user_id = fields.Integer(dump_only=True)
    first_name = fields.String(validate=validate.Length(max=64))
    last_name = fields.String(validate=validate.Length(max=64))
    email = fields.Email(dump_only=True)
    phone = fields.String(validate=validate.Length(max=32), allow_none=True)
    headline = fields.String(validate=validate.Length(max=128), allow_none=True)
    summary = fields.String(allow_none=True)
    location = fields.String(validate=validate.Length(max=128), allow_none=True)
    country = fields.String(allow_none=True)
    city = fields.String(allow_none=True)
    years_of_experience = fields.Float()
    highest_education_level = fields.String(allow_none=True)
    
    linkedin_url = fields.String(allow_none=True)
    github_url = fields.String(allow_none=True)
    portfolio_url = fields.String(allow_none=True)
    website_url = fields.String(allow_none=True)
    
    resume_quality_score = fields.Float(dump_only=True)
    quality_breakdown = fields.Dict(dump_only=True)
    
    skills = fields.Nested(CandidateSkillSchema, many=True)
    experiences = fields.Nested(ExperienceSchema, many=True)
    educations = fields.Nested(EducationSchema, many=True)
    certifications = fields.Nested(CandidateCertificationSchema, many=True)
    projects = fields.Nested(CandidateProjectSchema, many=True)
    notes = fields.Nested(CandidateNoteSchema, many=True, dump_only=True)
    created_at = fields.DateTime(dump_only=True)
