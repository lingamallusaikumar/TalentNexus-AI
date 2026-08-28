import pytest
from app.matching.services import evaluate_and_save_match
from app.candidates.models import Candidate, CandidateSkill
from app.jobs.models import Job, JobRequirement
from app.organizations.models import Organization
from app.users.models import User, Role
from app.extensions import db

def test_semantic_match(app):
    with app.app_context():
        org = Organization(name="Org")
        role = Role(name="Cand")
        db.session.add_all([org, role])
        db.session.commit()
        
        user = User(email="testm@t.com", password="pwd", first_name="A", last_name="B", role_id=role.id)
        db.session.add(user)
        db.session.commit()
        
        cand = Candidate(user_id=user.id, summary="I am a Python Backend Developer.")
        job = Job(organization_id=org.id, title="Backend Dev", description="Looking for a Python Developer for Backend.")
        db.session.add_all([cand, job])
        db.session.commit()
        
        # Add required skills
        req1 = JobRequirement(job_id=job.id, skill_name="Python", weight=1.0)
        cskill1 = CandidateSkill(candidate_id=cand.id, skill_name="Python")
        
        db.session.add_all([req1, cskill1])
        db.session.commit()
        
        match_record = evaluate_and_save_match(cand, job)
        
        assert match_record.id is not None
        assert match_record.score > 0
        assert "overall_score" in match_record.explanation
        assert len(match_record.explanation["strengths"]) == 1
        assert "Python" in match_record.explanation["strengths"][0]
