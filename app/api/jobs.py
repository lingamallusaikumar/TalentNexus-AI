from flask import Blueprint, request, jsonify
from app.jobs.models import Job, JobRequirement
from app.auth.utils import token_required
from app.extensions import db
from app.common.errors import APIError
from ml.job_intelligence.analyzer import JobDescriptionIntelligence
from app.skills.service import SkillNormalizationEngine

jobs_bp = Blueprint('jobs', __name__)

@jobs_bp.route('', methods=['GET'])
@token_required
def list_jobs(current_user):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    status = request.args.get('status')
    
    query = Job.query.filter_by(is_deleted=False)
    if current_user.current_organization_id:
        query = query.filter_by(organization_id=current_user.current_organization_id)
        
    if status:
        query = query.filter_by(status=status.upper())
        
    pagination = query.order_by(Job.created_at.desc()).paginate(page=page, per_page=per_page, error_out=False)
    
    items = []
    for j in pagination.items:
        items.append({
            "id": j.id,
            "title": j.title,
            "department_id": j.department_id,
            "location": j.location,
            "is_remote": j.is_remote,
            "employment_type": j.employment_type,
            "status": j.status,
            "salary_min": j.salary_min,
            "salary_max": j.salary_max,
            "requirements_count": len(j.requirements)
        })
        
    return jsonify({
        "jobs": items,
        "total": pagination.total,
        "page": pagination.page,
        "pages": pagination.pages
    }), 200

@jobs_bp.route('', methods=['POST'])
@token_required
def create_job(current_user):
    data = request.get_json()
    if not data or not data.get('title') or not data.get('description'):
        raise APIError("Job title and description are required", status_code=400)
        
    org_id = current_user.current_organization_id or 1
    
    # Run AI Job Intelligence analysis
    analysis = JobDescriptionIntelligence.analyze_job_description(data['title'], data['description'])
    
    job = Job(
        organization_id=org_id,
        created_by_user_id=current_user.id,
        title=data['title'],
        description=data['description'],
        location=data.get('location'),
        is_remote=data.get('is_remote', False),
        employment_type=data.get('employment_type', 'FULL_TIME'),
        salary_min=data.get('salary_min'),
        salary_max=data.get('salary_max'),
        status='PUBLISHED',
        description_quality_score=analysis['quality_score'],
        inclusive_language_score=analysis['inclusive_score'],
        jd_analysis=analysis
    )
    db.session.add(job)
    db.session.commit()
    
    # Add requirements (either from payload or auto-extracted by AI)
    reqs_input = data.get('requirements')
    if reqs_input and isinstance(reqs_input, list):
        for req in reqs_input:
            canonical = SkillNormalizationEngine.normalize_skill(req.get('skill_name', ''))
            if canonical:
                job_req = JobRequirement(
                    job_id=job.id,
                    skill_name=canonical,
                    is_required=req.get('is_required', True),
                    min_years_experience=req.get('min_years_experience', 1.0),
                    weight=req.get('weight', 1.0)
                )
                db.session.add(job_req)
    else:
        # Fallback to AI extracted skills
        for sk in analysis['extracted_skills']:
            job_req = JobRequirement(
                job_id=job.id,
                skill_name=sk['skill_name'],
                is_required=True,
                weight=1.0
            )
            db.session.add(job_req)
            
    db.session.commit()
    
    return jsonify({
        "message": "Job created successfully",
        "job_id": job.id,
        "quality_score": job.description_quality_score,
        "inclusive_score": job.inclusive_language_score
    }), 201
