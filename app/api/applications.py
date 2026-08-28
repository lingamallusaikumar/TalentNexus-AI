from flask import Blueprint, request, jsonify
from app.applications.models import Application, ApplicationHistory
from app.candidates.models import Candidate
from app.jobs.models import Job
from app.auth.utils import token_required
from app.extensions import db
from app.common.errors import APIError
from app.matching.services import evaluate_and_save_match

applications_bp = Blueprint('applications', __name__)

@applications_bp.route('/apply', methods=['POST'])
@token_required
def apply_to_job(current_user):
    data = request.get_json()
    if not data or not data.get('job_id'):
        raise APIError("job_id is required", status_code=400)
        
    candidate = current_user.candidate_profile
    if not candidate:
        raise APIError("User must have a candidate profile to apply", status_code=400)
        
    job = Job.query.get_or_404(data['job_id'])
    
    existing = Application.query.filter_by(candidate_id=candidate.id, job_id=job.id).first()
    if existing:
        raise APIError("Candidate has already applied to this job", status_code=400)
        
    application = Application(
        candidate_id=candidate.id,
        job_id=job.id,
        current_stage='Applied',
        source=data.get('source', 'CAREERS_PORTAL')
    )
    db.session.add(application)
    db.session.commit()
    
    # Auto evaluate matching score
    evaluate_and_save_match(candidate, job)
    
    # Log stage entry
    history = ApplicationHistory(
        application_id=application.id,
        from_stage=None,
        to_stage='Applied',
        notes='Application submitted'
    )
    db.session.add(history)
    db.session.commit()
    
    return jsonify({
        "message": "Application submitted successfully",
        "application_id": application.id,
        "current_stage": application.current_stage
    }), 201

@applications_bp.route('/<int:application_id>/move-stage', methods=['POST'])
@token_required
def move_application_stage(current_user, application_id):
    data = request.get_json()
    if not data or not data.get('target_stage'):
        raise APIError("target_stage is required", status_code=400)
        
    app_record = Application.query.get_or_404(application_id)
    old_stage = app_record.current_stage
    target_stage = data['target_stage']
    
    app_record.current_stage = target_stage
    history = ApplicationHistory(
        application_id=app_record.id,
        moved_by_user_id=current_user.id,
        from_stage=old_stage,
        to_stage=target_stage,
        notes=data.get('notes', 'Manual stage movement by recruiter')
    )
    db.session.add(history)
    db.session.commit()
    
    return jsonify({
        "message": f"Candidate moved from {old_stage} to {target_stage}",
        "application_id": app_record.id,
        "current_stage": app_record.current_stage
    }), 200
