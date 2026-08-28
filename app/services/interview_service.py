from datetime import datetime
from app.extensions import db
from app.interviews.models import Interview, Interviewer, InterviewFeedback
from app.events.bus import EventBus, EVENT_INTERVIEW_SCHEDULED
from app.common.errors import APIError

class InterviewService:
    """Manages multi-round interview scheduling, panels, and scorecard feedback aggregation."""

    @classmethod
    def schedule_interview(cls, application_id: int, title: str, scheduled_at: datetime, interviewer_ids: list[int], duration_minutes: int = 60, meeting_link: str = None, location: str = None) -> Interview:
        interview = Interview(
            application_id=application_id,
            title=title,
            scheduled_at=scheduled_at,
            duration_minutes=duration_minutes,
            meeting_link=meeting_link,
            location=location,
            status='SCHEDULED'
        )
        db.session.add(interview)
        db.session.commit()
        
        for idx, u_id in enumerate(interviewer_ids):
            panel = Interviewer(
                interview_id=interview.id,
                user_id=u_id,
                is_lead=(idx == 0)
            )
            db.session.add(panel)
            
        db.session.commit()
        
        EventBus.publish(
            event_name=EVENT_INTERVIEW_SCHEDULED,
            entity_type='Interview',
            entity_id=interview.id,
            payload={
                "interview_id": interview.id,
                "application_id": application_id,
                "scheduled_at": str(scheduled_at),
                "title": title
            }
        )
        return interview

    @classmethod
    def submit_feedback(cls, interview_id: int, interviewer_id: int, rating: int, notes: str, recommendation: str, criteria_ratings: dict = None, strengths: str = None, improvements: str = None) -> InterviewFeedback:
        feedback = InterviewFeedback(
            interview_id=interview_id,
            interviewer_id=interviewer_id,
            overall_rating=rating,
            notes=notes,
            recommendation=recommendation,
            criteria_ratings=criteria_ratings or {},
            strengths=strengths,
            areas_for_improvement=improvements
        )
        db.session.add(feedback)
        db.session.commit()
        
        # Check if all panelists submitted feedback to update final interview status
        interview = Interview.query.get(interview_id)
        if interview:
            feedbacks = interview.feedbacks
            if len(feedbacks) >= len(interview.panel_members):
                interview.status = 'COMPLETED'
                # Compute composite recommendation
                recs = [f.recommendation for f in feedbacks]
                if 'STRONG_NO' in recs:
                    interview.final_recommendation = 'STRONG_NO'
                elif recs.count('STRONG_HIRE') >= 2:
                    interview.final_recommendation = 'STRONG_HIRE'
                else:
                    interview.final_recommendation = feedbacks[0].recommendation
                db.session.commit()
                
        return feedback
