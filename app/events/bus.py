import logging
from datetime import datetime
from app.extensions import db
from app.events.models import EventLog

logger = logging.getLogger(__name__)

# Standard System Event Constants
EVENT_RESUME_UPLOADED = 'resume.uploaded'
EVENT_RESUME_PARSING_STARTED = 'resume.parsing.started'
EVENT_RESUME_PARSED = 'resume.parsed'
EVENT_CANDIDATE_PROFILE_UPDATED = 'candidate.profile.updated'
EVENT_JOB_CREATED = 'job.created'
EVENT_JOB_UPDATED = 'job.updated'
EVENT_CANDIDATE_MATCH_REQUESTED = 'candidate.match.requested'
EVENT_CANDIDATE_MATCH_COMPLETED = 'candidate.match.completed'
EVENT_CANDIDATE_SCORE_UPDATED = 'candidate.score.updated'
EVENT_CANDIDATE_RANK_CHANGED = 'candidate.rank.changed'
EVENT_INTERVIEW_SCHEDULED = 'interview.scheduled'
EVENT_ASSESSMENT_COMPLETED = 'assessment.completed'
EVENT_NOTIFICATION_CREATED = 'notification.created'

class EventBus:
    _listeners = {}

    @classmethod
    def subscribe(cls, event_name, handler):
        if event_name not in cls._listeners:
            cls._listeners[event_name] = []
        cls._listeners[event_name].append(handler)

    @classmethod
    def publish(cls, event_name: str, entity_type: str, entity_id: int, organization_id: int = None, actor_user_id: int = None, payload: dict = None):
        """
        Publishes an event synchronously to local subscribers and asynchronously logs to EventLog.
        Also triggers workflow engine if applicable.
        """
        try:
            event_log = EventLog(
                event_name=event_name,
                entity_type=entity_type,
                entity_id=entity_id,
                organization_id=organization_id,
                actor_user_id=actor_user_id,
                payload=payload or {},
                status='PUBLISHED'
            )
            db.session.add(event_log)
            db.session.commit()
        except Exception as e:
            logger.error(f"Failed to persist event log for {event_name}: {e}")

        # Trigger workflow evaluation
        try:
            if organization_id:
                from app.workflows.engine import process_event
                process_event(
                    organization_id=organization_id,
                    trigger_event=event_name,
                    target_entity_type=entity_type,
                    target_entity_id=entity_id,
                    context=payload or {}
                )
        except Exception as e:
            logger.error(f"Error processing workflow hooks for event {event_name}: {e}")

        # Dispatch to in-process subscribers
        handlers = cls._listeners.get(event_name, [])
        for handler in handlers:
            try:
                handler(event_name=event_name, entity_type=entity_type, entity_id=entity_id, payload=payload)
            except Exception as e:
                logger.error(f"Error executing listener {handler} for {event_name}: {e}")
