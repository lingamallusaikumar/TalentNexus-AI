from app.extensions import db
from app.matching.models import CandidateMatch, ScoringProfile, RankingHistory
from ml.matching.scorer import CandidateMatchingEngine
from app.realtime.socketio import emit_ranking_update
from app.events.bus import EventBus, EVENT_CANDIDATE_SCORE_UPDATED, EVENT_CANDIDATE_RANK_CHANGED

def evaluate_and_save_match(candidate, job, scoring_profile_id=None):
    """
    Evaluates candidate against job, persists match record, updates rankings, and broadcasts websocket updates.
    """
    scoring_profile = ScoringProfile.query.get(scoring_profile_id) if scoring_profile_id else None
    result = CandidateMatchingEngine.calculate_match(candidate, job, scoring_profile)
    
    match_record = CandidateMatch.query.filter_by(
        candidate_id=candidate.id, 
        job_id=job.id
    ).first()
    
    if not match_record:
        match_record = CandidateMatch(candidate_id=candidate.id, job_id=job.id)
        db.session.add(match_record)
        
    match_record.overall_score = result['overall_score']
    match_record.recommendation = result['recommendation']
    
    sub = result['sub_scores']
    match_record.score_skills = sub['skills_score']
    match_record.score_semantic = sub['semantic_similarity_score']
    match_record.score_experience = sub['experience_score']
    match_record.score_projects = sub['projects_score']
    match_record.score_education = sub['education_score']
    match_record.score_certifications = sub['certifications_score']
    match_record.score_location = sub['location_score']
    match_record.score_preferences = sub['preferences_score']
    
    match_record.explanation = result['explanation']
    db.session.commit()
    
    # Recalculate ranks for this job
    recalculate_job_rankings(job.id)
    
    # Emit event and WebSockets
    EventBus.publish(
        event_name=EVENT_CANDIDATE_SCORE_UPDATED,
        entity_type='CandidateMatch',
        entity_id=match_record.id,
        organization_id=job.organization_id,
        payload={
            "job_id": job.id,
            "candidate_id": candidate.id,
            "overall_score": match_record.overall_score,
            "recommendation": match_record.recommendation
        }
    )
    
    emit_ranking_update(job.id)
    return match_record

def recalculate_job_rankings(job_id: int):
    """Recalculates rank positions for all candidates evaluated for a job."""
    matches = CandidateMatch.query.filter_by(job_id=job_id).order_by(CandidateMatch.overall_score.desc()).all()
    
    for rank_idx, m in enumerate(matches, start=1):
        if m.rank_position != rank_idx:
            history = RankingHistory(
                job_id=job_id,
                candidate_id=m.candidate_id,
                previous_rank=m.rank_position,
                new_rank=rank_idx,
                previous_score=m.overall_score,
                new_score=m.overall_score,
                trigger_event='SCORE_RECALCULATION'
            )
            db.session.add(history)
            m.rank_position = rank_idx
            
    db.session.commit()
