import pytest
from app.extensions import db
from app.organizations.models import Organization
from app.workflows.models import WorkflowRule
from app.workflows.engine import process_event
from app.applications.models import Application
from app.jobs.models import Job
from app.candidates.models import Candidate
from app.users.models import User, Role

def test_workflow_engine(app):
    with app.app_context():
        # Setup
        org = Organization(name="Org")
        role = Role(name="C")
        db.session.add_all([org, role])
        db.session.commit()
        
        user = User(email="w@w.com", password="pwd", first_name="A", last_name="B", role_id=role.id)
        db.session.add(user)
        db.session.commit()
        
        cand = Candidate(user_id=user.id)
        job = Job(organization_id=org.id, title="Dev", description="Code")
        db.session.add_all([cand, job])
        db.session.commit()
        
        application = Application(candidate_id=cand.id, job_id=job.id, current_stage="Applied")
        db.session.add(application)
        
        # Rule
        rule = WorkflowRule(
            organization_id=org.id,
            name="Auto Shortlist High Score",
            trigger_event="candidate.match.completed",
            conditions=[{"field": "score", "operator": ">=", "value": 85}],
            actions=[{"type": "move_stage", "target": "Shortlisted"}]
        )
        db.session.add(rule)
        db.session.commit()
        
        # Emit event
        context = {"score": 90}
        process_event(org.id, "candidate.match.completed", "Application", application.id, context)
        
        # Verify
        db.session.refresh(application)
        assert application.current_stage == "Shortlisted"
        assert len(application.history) == 1
