from marshmallow import Schema, fields, validate, post_load

class UserRegisterSchema(Schema):
    email = fields.Email(required=True, validate=validate.Length(max=128))
    password = fields.String(required=True, validate=validate.Length(min=8, max=128))
    first_name = fields.String(required=True, validate=validate.Length(min=1, max=64))
    last_name = fields.String(required=True, validate=validate.Length(min=1, max=64))
    phone = fields.String(validate=validate.Length(max=32), allow_none=True)
    role = fields.String(validate=validate.OneOf([
        'Super Admin', 'Organization Admin', 'HR Manager', 
        'Recruiter', 'Hiring Manager', 'Interviewer', 'Candidate'
    ]), missing='Candidate')
    organization_name = fields.String(validate=validate.Length(min=2, max=128), allow_none=True)

class UserLoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)
    two_factor_code = fields.String(validate=validate.Length(equal=6), allow_none=True)

class PasswordResetRequestSchema(Schema):
    email = fields.Email(required=True)

class PasswordResetConfirmSchema(Schema):
    token = fields.String(required=True)
    new_password = fields.String(required=True, validate=validate.Length(min=8, max=128))

class UserResponseSchema(Schema):
    id = fields.Integer()
    email = fields.Email()
    first_name = fields.String()
    last_name = fields.String()
    full_name = fields.String()
    phone = fields.String()
    is_active = fields.Boolean()
    is_verified = fields.Boolean()
    two_factor_enabled = fields.Boolean()
    role = fields.Method("get_role_name")
    organization_id = fields.Integer(attribute="current_organization_id")
    created_at = fields.DateTime()

    def get_role_name(self, obj):
        return obj.role.name if obj.role else None

class OrganizationSchema(Schema):
    id = fields.Integer()
    name = fields.String(required=True, validate=validate.Length(min=2, max=128))
    slug = fields.String()
    domain = fields.String(allow_none=True)
    is_active = fields.Boolean()
    branding = fields.Dict()
    settings = fields.Dict()
    created_at = fields.DateTime()

class InvitationSchema(Schema):
    id = fields.Integer()
    email = fields.Email(required=True)
    role_id = fields.Integer(required=True)
    status = fields.String()
    expires_at = fields.DateTime()
    created_at = fields.DateTime()
