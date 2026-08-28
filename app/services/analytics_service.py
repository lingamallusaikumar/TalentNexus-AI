from sqlalchemy import func
from app.extensions import db
from app.applications.models import Application, ApplicationHistory
from app.jobs.models import Job, JobRequirement
from app.candidates.models import Candidate, CandidateSkill
from app.skills.models import Skill

class AdvancedAnalyticsService:
    """Enterprise recruitment intelligence analytics, SLA reporting, and skill demand matrices."""

    @classmethod
    def calculate_time_to_hire_days(cls, organization_id: int) -> float:
        """Calculates average days from application submission to hired stage."""
        hired_apps = Application.query.join(Job).filter(
            Job.organization_id == organization_id,
            Application.status == 'HIRED'
        ).all()
        
        if not hired_apps:
            return 21.5 # Default benchmark
            
        durations = []
        for app in hired_apps:
            if app.history:
                hired_entry = [h for h in app.history if h.to_stage == 'Hired']
                if hired_entry:
                    days = (hired_entry[0].created_at - app.applied_at).total_seconds() / 86400.0
                    durations.append(days)
                    
        return round(sum(durations) / len(durations), 1) if durations else 21.5

    @classmethod
    def get_skill_demand_matrix(cls, organization_id: int) -> list[dict]:
        """Calculates demand (jobs requiring skill) vs supply (candidates possessing skill)."""
        job_skills = db.session.query(
            JobRequirement.skill_name,
            func.count(JobRequirement.id).label('demand_count')
        ).join(Job).filter(
            Job.organization_id == organization_id,
            Job.status == 'PUBLISHED'
        ).group_by(JobRequirement.skill_name).all()
        
        matrix = []
        for skill_name, demand in job_skills:
            supply = CandidateSkill.query.filter(
                CandidateSkill.skill_name.ilike(skill_name)
            ).count()
            
            ratio = round(demand / max(supply, 1), 2)
            matrix.append({
                "skill_name": skill_name,
                "job_demand_count": demand,
                "candidate_supply_count": supply,
                "demand_supply_ratio": ratio,
                "market_scarcity": "HIGH" if ratio >= 1.5 else ("BALANCED" if ratio >= 0.5 else "ABUNDANT")
            })
            
        matrix.sort(key=lambda x: x['job_demand_count'], reverse=True)
        return matrix
