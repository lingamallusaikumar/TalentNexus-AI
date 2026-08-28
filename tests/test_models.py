import pytest
from datetime import date
from app.extensions import db
from app.organizations.models import Organization
from app.users.models import User, Role
from app.candidates.models import Candidate, Experience
from app.jobs.models import Job, JobRequirement

def test_candidate_model(app):
    with app.app_context():
        # Setup Org, Role, User
        org = Organization(name="Test Org")
        role = Role(name="Candidate")
        db.session.add_all([org, role])
        db.session.commit()
        
        user = User(email="test_cand@test.com", password="pwd", first_name="A", last_name="B", role_id=role.id, organization_id=org.id)
        db.session.add(user)
        db.session.commit()
        
        # Test Candidate
        candidate = Candidate(user_id=user.id, phone="1234567890", summary="A good dev")
        db.session.add(candidate)
        db.session.commit()
        
        # Test Experience
        exp = Experience(candidate_id=candidate.id, company="TechCorp", title="Dev", start_date=date(2020, 1, 1))
        db.session.add(exp)
        db.session.commit()
        
        assert candidate.id is not None
        assert candidate.user.email == "test_cand@test.com"
        assert len(candidate.experiences) == 1
        assert candidate.experiences[0].company == "TechCorp"

def test_job_model(app):
    with app.app_context():
        org = Organization(name="Test Org")
        db.session.add(org)
        db.session.commit()
        
        job = Job(organization_id=org.id, title="Python Dev", description="Write Python", status="Published")
        db.session.add(job)
        db.session.commit()
        
        req = JobRequirement(job_id=job.id, skill_name="Python", min_years_experience=3.0)
        db.session.add(req)
        db.session.commit()
        
        assert job.id is not None
        assert len(job.requirements) == 1
        assert job.requirements[0].skill_name == "Python"
