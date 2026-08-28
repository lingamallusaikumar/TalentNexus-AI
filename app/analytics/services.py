from sqlalchemy import func
from app.extensions import db
from app.applications.models import Application
from app.jobs.models import Job
from app.interviews.models import Interview

def get_recruitment_funnel_metrics(organization_id: int):
    """
    Returns funnel metrics for an organization.
    """
    # Total Active Jobs
    active_jobs = db.session.query(func.count(Job.id)).filter(
        Job.organization_id == organization_id,
        Job.status == 'Published'
    ).scalar()
    
    # Total Applications for those jobs
    total_applications = db.session.query(func.count(Application.id)).join(Job).filter(
        Job.organization_id == organization_id
    ).scalar()
    
    # Applications by Stage
    stage_counts = db.session.query(
        Application.current_stage, 
        func.count(Application.id)
    ).join(Job).filter(
        Job.organization_id == organization_id
    ).group_by(Application.current_stage).all()
    
    stages = {stage: count for stage, count in stage_counts}
    
    # Upcoming Interviews
    upcoming_interviews = db.session.query(func.count(Interview.id)).join(
        Application
    ).join(
        Job
    ).filter(
        Job.organization_id == organization_id,
        Interview.status == 'Scheduled'
    ).scalar()
    
    # Shortlisting Rate
    total_screened = total_applications
    total_shortlisted = stages.get('Shortlisted', 0) + stages.get('Interview', 0) + stages.get('Offer', 0) + stages.get('Hired', 0)
    
    shortlist_rate = 0
    if total_screened and total_screened > 0:
        shortlist_rate = (total_shortlisted / total_screened) * 100
        
    return {
        "active_jobs": active_jobs or 0,
        "total_applications": total_applications or 0,
        "funnel_by_stage": stages,
        "upcoming_interviews": upcoming_interviews or 0,
        "shortlist_rate_percentage": round(shortlist_rate, 2)
    }
