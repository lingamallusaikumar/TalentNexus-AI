from app.matching.models import CandidateMatch
from ml.matching.scorer import calculate_candidate_match
from app.extensions import db

def evaluate_and_save_match(candidate, job):
    """
    Evaluates a candidate against a job, generates a score and explanation, 
    and saves it to the database.
    """
    result = calculate_candidate_match(candidate, job)
    
    match_record = CandidateMatch.query.filter_by(
        candidate_id=candidate.id, 
        job_id=job.id
    ).first()
    
    if not match_record:
        match_record = CandidateMatch(candidate_id=candidate.id, job_id=job.id)
        db.session.add(match_record)
        
    match_record.score = result['score']
    match_record.explanation = result['explanation']
    
    db.session.commit()
    
    return match_record
