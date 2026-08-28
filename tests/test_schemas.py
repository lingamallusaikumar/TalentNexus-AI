import pytest
from app.schemas.auth_schemas import UserRegisterSchema, UserLoginSchema
from app.schemas.job_schemas import JobCreateSchema

def test_user_register_schema_validation():
    schema = UserRegisterSchema()
    
    # Valid
    valid_data = {
        "email": "dev@enterprise.com",
        "password": "Password123!",
        "first_name": "John",
        "last_name": "Doe",
        "role": "Recruiter"
    }
    errors = schema.validate(valid_data)
    assert len(errors) == 0

    # Invalid email
    invalid_data = {
        "email": "not-an-email",
        "password": "short",
        "first_name": "",
        "last_name": ""
    }
    errors = schema.validate(invalid_data)
    assert "email" in errors
    assert "password" in errors

def test_job_create_schema_validation():
    schema = JobCreateSchema()
    valid_job = {
        "title": "Staff Backend Engineer",
        "description": "Comprehensive job description requiring high-scale distributed systems expertise.",
        "location": "New York, NY",
        "is_remote": True,
        "requirements": [
            {"skill_name": "Python", "is_required": True, "min_years_experience": 5.0}
        ]
    }
    errors = schema.validate(valid_job)
    assert len(errors) == 0
