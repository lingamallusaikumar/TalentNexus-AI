from flask import Blueprint, request, jsonify
from app.candidates.models import Candidate, CandidateSkill, Experience, Education
from app.auth.utils import token_required
from app.extensions import db
from app.common.errors import APIError

candidates_bp = Blueprint('candidates', __name__)

@candidates_bp.route('', methods=['GET'])
@token_required
def list_candidates(current_user):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    search = request.args.get('search', '').strip()
    
    query = Candidate.query.filter_by(is_deleted=False)
    if search:
        query = query.filter(
            (Candidate.first_name.ilike(f"%{search}%")) |
            (Candidate.last_name.ilike(f"%{search}%")) |
            (Candidate.headline.ilike(f"%{search}%")) |
            (Candidate.location.ilike(f"%{search}%"))
        )
        
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    
    items = []
    for c in pagination.items:
        items.append({
            "id": c.id,
            "name": f"{c.first_name or ''} {c.last_name or ''}".strip(),
            "email": c.email,
            "headline": c.headline,
            "location": c.location,
            "years_of_experience": c.years_of_experience,
            "resume_quality_score": c.resume_quality_score,
            "skills": [s.skill_name for s in c.skills]
        })
        
    return jsonify({
        "candidates": items,
        "total": pagination.total,
        "page": pagination.page,
        "pages": pagination.pages
    }), 200

@candidates_bp.route('/<int:candidate_id>', methods=['GET'])
@token_required
def get_candidate(current_user, candidate_id):
    candidate = Candidate.query.get_or_404(candidate_id)
    return jsonify({
        "id": candidate.id,
        "first_name": candidate.first_name,
        "last_name": candidate.last_name,
        "email": candidate.email,
        "phone": candidate.phone,
        "headline": candidate.headline,
        "summary": candidate.summary,
        "location": candidate.location,
        "years_of_experience": candidate.years_of_experience,
        "resume_quality_score": candidate.resume_quality_score,
        "quality_breakdown": candidate.quality_breakdown,
        "skills": [{
            "id": s.id,
            "skill_name": s.skill_name,
            "years_of_experience": s.years_of_experience,
            "proficiency": s.proficiency
        } for s in candidate.skills],
        "experiences": [{
            "id": e.id,
            "company": e.company,
            "title": e.title,
            "start_date": str(e.start_date),
            "end_date": str(e.end_date) if e.end_date else None,
            "is_current": e.is_current,
            "description": e.description
        } for e in candidate.experiences],
        "educations": [{
            "id": ed.id,
            "institution": ed.institution,
            "degree": ed.degree,
            "field_of_study": ed.field_of_study
        } for ed in candidate.educations]
    }), 200
