from datetime import datetime, timedelta
from app.extensions import db
from app.applications.models import Application, ApplicationHistory, RecruitmentPipeline, PipelineStage
from app.events.bus import EventBus
from app.common.errors import APIError
import logging

logger = logging.getLogger(__name__)

class ATSService:
    """Manages ATS candidate stage progression, SLA tracking, and rejection handling."""

    @classmethod
    def move_candidate_stage(cls, application_id: int, target_stage: str, actor_user_id: int = None, notes: str = None, is_automated: bool = False) -> Application:
        app_record = Application.query.get_or_404(application_id)
        old_stage = app_record.current_stage
        
        if old_stage == target_stage:
            return app_record
            
        app_record.current_stage = target_stage
        app_record.stage_entered_at = datetime.utcnow()
        app_record.is_sla_breached = False
        app_record.sla_deadline = datetime.utcnow() + timedelta(hours=48)
        
        if target_stage == 'Hired':
            app_record.status = 'HIRED'
        elif target_stage == 'Rejected':
            app_record.status = 'REJECTED'
            app_record.rejected_at = datetime.utcnow()

        history = ApplicationHistory(
            application_id=app_record.id,
            moved_by_user_id=actor_user_id,
            from_stage=old_stage,
            to_stage=target_stage,
            notes=notes or f"Moved from {old_stage} to {target_stage}",
            is_automated=is_automated
        )
        db.session.add(history)
        db.session.commit()
        
        # Publish event
        EventBus.publish(
            event_name='application.stage.changed',
            entity_type='Application',
            entity_id=app_record.id,
            organization_id=app_record.job.organization_id if app_record.job else None,
            actor_user_id=actor_user_id,
            payload={
                "application_id": app_record.id,
                "candidate_id": app_record.candidate_id,
                "job_id": app_record.job_id,
                "from_stage": old_stage,
                "to_stage": target_stage
            }
        )
        
        return app_record

    @classmethod
    def reject_candidate(cls, application_id: int, reason: str, notes: str = None, actor_user_id: int = None) -> Application:
        app_record = Application.query.get_or_404(application_id)
        app_record.current_stage = 'Rejected'
        app_record.status = 'REJECTED'
        app_record.rejection_reason = reason
        app_record.rejection_notes = notes
        app_record.rejected_at = datetime.utcnow()
        
        history = ApplicationHistory(
            application_id=app_record.id,
            moved_by_user_id=actor_user_id,
            from_stage=app_record.current_stage,
            to_stage='Rejected',
            notes=f"Rejection Reason: {reason}. {notes or ''}",
            is_automated=False
        )
        db.session.add(history)
        db.session.commit()
        return app_record

    @classmethod
    def check_sla_breaches(cls) -> list[int]:
        """Scans active applications and marks SLA breaches for recruiter action."""
        now = datetime.utcnow()
        breached_apps = Application.query.filter(
            Application.status == 'ACTIVE',
            Application.is_sla_breached == False,
            Application.sla_deadline < now
        ).all()
        
        breached_ids = []
        for app in breached_apps:
            app.is_sla_breached = True
            breached_ids.append(app.id)
            
        db.session.commit()
        return breached_ids
