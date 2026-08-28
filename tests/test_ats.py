import pytest
from datetime import datetime
from app.extensions import db
from app.applications.models import Application, ApplicationHistory
from app.interviews.models import Interview, Interviewer, InterviewFeedback
from app.candidates.models import Candidate
from app.jobs.models import Job
from app.users.models import User, Role
from app.organizations.models import Organization

def test_application_pipeline(app):
    with app.app_context():
        # Setup basic data
        org = Organization(name="Test Org")
        role = Role(name="Candidate")
        db.session.add_all([org, role])
        db.session.commit()
        
        user = User(email="applicant@test.com", password="pwd", first_name="A", last_name="B", role_id=role.id)
        db.session.add(user)
        db.session.commit()
        
        cand = Candidate(user_id=user.id)
        job = Job(organization_id=org.id, title="Frontend Dev", description="HTML CSS JS")
        db.session.add_all([cand, job])
        db.session.commit()
        
        # Test Application
        application = Application(candidate_id=cand.id, job_id=job.id, current_stage="Applied")
        db.session.add(application)
        db.session.commit()
        
        # Test Stage Move History
        history = ApplicationHistory(application_id=application.id, from_stage="Applied", to_stage="AI Screening")
        application.current_stage = "AI Screening"
        db.session.add(history)
        db.session.commit()
        
        assert application.current_stage == "AI Screening"
        assert len(application.history) == 1
        
        # Test Interview scheduling
        interview = Interview(application_id=application.id, title="Technical Round 1", scheduled_at=datetime.utcnow())
        db.session.add(interview)
        db.session.commit()
        
        assert interview.id is not None
        assert len(application.interviews) == 1
