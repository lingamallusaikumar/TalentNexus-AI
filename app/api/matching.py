from flask import Blueprint, request, jsonify
from app.matching.models import CandidateMatch
from app.matching.services import evaluate_and_save_match
from app.candidates.models import Candidate
from app.jobs.models import Job
from app.auth.utils import token_required
from app.common.errors import APIError
from app.extensions import db

matching_bp = Blueprint('matching', __name__)

@matching_bp.route('/evaluate', methods=['POST'])
@token_required
def evaluate_match_endpoint(current_user):
    data = request.get_json()
    if not data or not data.get('candidate_id') or not data.get('job_id'):
        raise APIError("Both candidate_id and job_id are required", status_code=400)
        
    candidate = Candidate.query.get_or_404(data['candidate_id'])
    job = Job.query.get_or_404(data['job_id'])
    
    match = evaluate_and_save_match(candidate, job, data.get('scoring_profile_id'))
    
    return jsonify({
        "candidate_id": candidate.id,
        "job_id": job.id,
        "overall_score": match.overall_score,
        "recommendation": match.recommendation,
        "rank_position": match.rank_position,
        "explanation": match.explanation
    }), 200

@matching_bp.route('/job/<int:job_id>/rankings', methods=['GET'])
@token_required
def get_job_rankings(current_user, job_id):
    matches = CandidateMatch.query.filter_by(job_id=job_id).order_by(CandidateMatch.overall_score.desc()).all()
    
    results = []
    for m in matches:
        cand = m.candidate
        results.append({
            "rank": m.rank_position,
            "candidate_id": m.candidate_id,
            "name": f"{cand.first_name or ''} {cand.last_name or ''}".strip(),
            "headline": cand.headline,
            "score": m.overall_score,
            "recommendation": m.recommendation,
            "strengths": m.explanation.get('strengths', []) if m.explanation else [],
            "weaknesses": m.explanation.get('weaknesses', []) if m.explanation else []
        })
        
    return jsonify({
        "job_id": job_id,
        "rankings": results
    }), 200

@matching_bp.route('/override', methods=['POST'])
@token_required
def override_ai_decision(current_user):
    data = request.get_json()
    if not data or not data.get('candidate_id') or not data.get('job_id') or not data.get('human_decision'):
        raise APIError("candidate_id, job_id, and human_decision are required", status_code=400)
        
    match = CandidateMatch.query.filter_by(candidate_id=data['candidate_id'], job_id=data['job_id']).first_or_404()
    
    match.is_overridden = True
    match.human_decision = data['human_decision']
    match.override_reason = data.get('override_reason', '')
    match.overridden_by_id = current_user.id
    db.session.commit()
    
    return jsonify({
        "message": "AI recommendation overridden successfully",
        "human_decision": match.human_decision
    }), 200
