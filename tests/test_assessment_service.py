import pytest
from app.services.assessment_service import AssessmentEvaluationService
from app.assessments.models import Assessment, AssessmentQuestion, AssessmentAttempt
from app.candidates.models import Candidate
from app.users.models import User, Role
from app.organizations.models import Organization
from app.extensions import db

def test_assessment_evaluation_service(app):
    with app.app_context():
        org = Organization(name="Test Org")
        role = Role(name="Candidate", code="CANDIDATE")
        db.session.add_all([org, role])
        db.session.commit()

        user = User(email="ass_cand@test.com", password="password", first_name="A", last_name="B", role_id=role.id)
        db.session.add(user)
        db.session.commit()

        cand = Candidate(user_id=user.id)
        db.session.add(cand)
        db.session.commit()

        assessment = Assessment(
            organization_id=org.id,
            title="Python Core Evaluation",
            passing_score_percentage=70.0
        )
        db.session.add(assessment)
        db.session.commit()

        q1 = AssessmentQuestion(
            assessment_id=assessment.id,
            question_text="What is the output of len([1, 2, 3])?",
            question_type="MCQ",
            points=50,
            options=[{"id": 1, "text": "2"}, {"id": 2, "text": "3"}, {"id": 3, "text": "4"}],
            correct_answer={"answer": 2}
        )
        q2 = AssessmentQuestion(
            assessment_id=assessment.id,
            question_text="Which of these are mutable?",
            question_type="MCQ",
            points=50,
            options=[{"id": 1, "text": "List"}, {"id": 2, "text": "Tuple"}, {"id": 3, "text": "String"}],
            correct_answer={"answer": 1}
        )
        db.session.add_all([q1, q2])
        db.session.commit()

        attempt = AssessmentAttempt(assessment_id=assessment.id, candidate_id=cand.id)
        db.session.add(attempt)
        db.session.commit()

        # Submit perfect score
        responses = {str(q1.id): 2, str(q2.id): 1}
        evaluated = AssessmentEvaluationService.evaluate_attempt(attempt.id, responses)
        assert evaluated.score_earned == 100.0
        assert evaluated.percentage_score == 100.0
        assert evaluated.is_passed == True
