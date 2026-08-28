import pytest
from app.services.candidate_service import CandidateService
from app.users.models import User, Role
from app.candidates.models import Candidate
from app.extensions import db

def test_candidate_service_lifecycle(app):
    with app.app_context():
        role = Role(name="Candidate", code="CANDIDATE")
        db.session.add(role)
        db.session.commit()

        user = User(email="test_service@example.com", password="password", first_name="John", last_name="Doe", role_id=role.id)
        db.session.add(user)
        db.session.commit()

        # 1. Test get_or_create_profile
        candidate = CandidateService.get_or_create_profile(user.id, {"first_name": "John", "last_name": "Doe", "headline": "Software Engineer"})
        assert candidate.id is not None
        assert candidate.headline == "Software Engineer"

        # 2. Test update_profile
        update_data = {
            "headline": "Lead Systems Architect",
            "years_of_experience": 8.0,
            "skills": [
                {"skill_name": "python", "years_of_experience": 8.0, "proficiency": "EXPERT"},
                {"skill_name": "flask", "years_of_experience": 5.0, "proficiency": "EXPERT"}
            ]
        }
        updated = CandidateService.update_profile(candidate.id, update_data, actor_id=user.id)
        assert updated.headline == "Lead Systems Architect"
        assert updated.years_of_experience == 8.0
        assert len(updated.skills) == 2
        assert updated.skills[0].skill_name in ["Python", "Flask"]

        # 3. Test add_note
        note = CandidateService.add_note(candidate.id, author_id=user.id, note_text="Strong problem solving ability in system design.")
        assert note.id is not None
        assert len(candidate.notes) == 1

        # 4. Test add_tag
        tag = CandidateService.add_tag(candidate.id, "top-tier-talent", actor_id=user.id)
        assert tag.tag == "top-tier-talent"
