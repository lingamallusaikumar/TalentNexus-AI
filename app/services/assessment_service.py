from datetime import datetime
from app.extensions import db
from app.assessments.models import Assessment, AssessmentQuestion, AssessmentAttempt
from app.events.bus import EventBus, EVENT_ASSESSMENT_COMPLETED
from app.common.errors import APIError

class AssessmentEvaluationService:
    """Evaluates candidate assessment attempts, auto-grades MCQs, and verifies passing criteria."""

    @classmethod
    def evaluate_attempt(cls, attempt_id: int, candidate_responses: dict) -> AssessmentAttempt:
        attempt = AssessmentAttempt.query.get_or_404(attempt_id)
        assessment = attempt.assessment
        
        questions = assessment.questions
        total_possible = sum([q.points for q in questions]) or 100.0
        earned_score = 0.0
        
        evaluations = {}
        
        for q in questions:
            q_id_str = str(q.id)
            candidate_ans = candidate_responses.get(q_id_str)
            
            is_correct = False
            points_awarded = 0
            
            if q.question_type == 'MCQ':
                correct_val = q.correct_answer.get('answer')
                if candidate_ans == correct_val:
                    is_correct = True
                    points_awarded = q.points
                    earned_score += q.points
            elif q.question_type == 'MULTI_SELECT':
                correct_set = set(q.correct_answer.get('answers', []))
                candidate_set = set(candidate_ans) if isinstance(candidate_ans, list) else set()
                if correct_set == candidate_set:
                    is_correct = True
                    points_awarded = q.points
                    earned_score += q.points
            else:
                # Coding / Essay fallback
                is_correct = True
                points_awarded = q.points
                earned_score += q.points
                
            evaluations[q_id_str] = {
                "question_id": q.id,
                "is_correct": is_correct,
                "points_awarded": points_awarded,
                "max_points": q.points,
                "explanation": q.explanation
            }
            
        percentage = (earned_score / total_possible) * 100.0 if total_possible > 0 else 0.0
        is_passed = percentage >= assessment.passing_score_percentage
        
        attempt.completed_at = datetime.utcnow()
        attempt.status = 'EVALUATED'
        attempt.score_earned = earned_score
        attempt.total_possible_score = total_possible
        attempt.percentage_score = round(percentage, 2)
        attempt.is_passed = is_passed
        attempt.responses = candidate_responses
        attempt.evaluations = evaluations
        
        db.session.commit()
        
        # Publish event
        EventBus.publish(
            event_name=EVENT_ASSESSMENT_COMPLETED,
            entity_type='AssessmentAttempt',
            entity_id=attempt.id,
            organization_id=assessment.organization_id,
            payload={
                "attempt_id": attempt.id,
                "candidate_id": attempt.candidate_id,
                "percentage_score": attempt.percentage_score,
                "is_passed": attempt.is_passed
            }
        )
        
        return attempt
