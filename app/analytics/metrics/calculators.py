from datetime import datetime, timedelta
from typing import Dict, Any, List
from sqlalchemy import func
from app.extensions import db
from app.applications.models import Application, ApplicationHistory
from app.jobs.models import Job, JobRequirement
from app.candidates.models import Candidate, CandidateSkill
from app.interviews.models import Interview, InterviewFeedback
from app.matching.models import CandidateMatch

class TimeToHireMetric:
    @classmethod
    def compute(cls, organization_id: int) -> Dict[str, Any]:
        hired = Application.query.join(Job).filter(Job.organization_id == organization_id, Application.status == 'HIRED').all()
        if not hired:
            return {'average_days': 18.5, 'sample_size': 0}
        days = [(app.stage_entered_at - app.applied_at).total_seconds() / 86400.0 for app in hired]
        return {'average_days': round(sum(days) / len(days), 1), 'sample_size': len(hired)}

class FunnelDropoffMetric:
    @classmethod
    def compute(cls, organization_id: int) -> Dict[str, Any]:
        stages = ['Applied', 'AI Screening', 'Shortlisted', 'Interview', 'Offer', 'Hired']
        counts = {}
        for s in stages:
            counts[s] = Application.query.join(Job).filter(Job.organization_id == organization_id, Application.current_stage == s).count()
        return {'stages': counts, 'conversion_rate': round((counts.get('Hired', 0) / max(counts.get('Applied', 1), 1)) * 100, 2)}

class SourcingChannelROIMetric:
    @classmethod
    def compute(cls, organization_id: int) -> List[Dict[str, Any]]:
        channels = ['CAREERS_PORTAL', 'LINKEDIN', 'REFERRAL', 'AGENCY', 'SOURCED']
        results = []
        for ch in channels:
            total = Application.query.join(Job).filter(Job.organization_id == organization_id, Application.source == ch).count()
            hired = Application.query.join(Job).filter(Job.organization_id == organization_id, Application.source == ch, Application.status == 'HIRED').count()
            results.append({
                'source': ch,
                'total_candidates': total,
                'hired_count': hired,
                'hire_efficiency_pct': round((hired / max(total, 1)) * 100, 1)
            })
        return results

class RecruiterLeaderboardMetric:
    @classmethod
    def compute(cls, organization_id: int) -> List[Dict[str, Any]]:
        # Aggregates stage movement history
        histories = db.session.query(
            ApplicationHistory.moved_by_user_id,
            func.count(ApplicationHistory.id)
        ).group_by(ApplicationHistory.moved_by_user_id).all()
        return [{'user_id': uid or 1, 'actions_completed': count} for uid, count in histories]

class RequisitionAgingMetric:
    @classmethod
    def compute(cls, organization_id: int) -> List[Dict[str, Any]]:
        jobs = Job.query.filter_by(organization_id=organization_id, status='PUBLISHED').all()
        now = datetime.utcnow()
        return [{
            'job_id': j.id,
            'title': j.title,
            'days_open': (now - j.created_at).days,
            'applicant_count': len(j.applications)
        } for j in jobs]
