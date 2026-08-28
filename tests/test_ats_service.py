import pytest
from app.services.ats_service import ATSService
from app.applications.models import Application
from app.jobs.models import Job
from app.candidates.models import Candidate
from app.users.models import User, Role
from app.organizations.models import Organization
from app.extensions import db

def test_ats_service_stage_transitions(app):
    with app.app_context():
        org = Organization(name="Test Org")
        role = Role(name="Candidate", code="CANDIDATE")
        db.session.add_all([org, role])
        db.session.commit()

        user = User(email="ats_cand@test.com", password="password", first_name="A", last_name="B", role_id=role.id)
        db.session.add(user)
        db.session.commit()

        cand = Candidate(user_id=user.id)
        job = Job(organization_id=org.id, title="Backend Dev", description="Write clean Python code")
        db.session.add_all([cand, job])
        db.session.commit()

        app_record = Application(candidate_id=cand.id, job_id=job.id, current_stage="Applied")
        db.session.add(app_record)
        db.session.commit()

        # 1. Test move_candidate_stage
        moved = ATSService.move_candidate_stage(app_record.id, "Shortlisted", actor_user_id=user.id, notes="Exceeded screening threshold")
        assert moved.current_stage == "Shortlisted"
        assert len(moved.history) == 1
        assert moved.history[0].to_stage == "Shortlisted"

        # 2. Test reject_candidate
        rejected = ATSService.reject_candidate(app_record.id, reason="Missing experience requirement", actor_user_id=user.id)
        assert rejected.current_stage == "Rejected"
        assert rejected.status == "REJECTED"
        assert rejected.rejection_reason == "Missing experience requirement"
