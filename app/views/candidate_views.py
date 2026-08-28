from flask import Blueprint, render_template
from app.candidates.models import Candidate

candidate_views_bp = Blueprint('candidate_views', __name__)

@candidate_views_bp.route('/candidates', methods=['GET'])
def list_candidates_page():
    candidates = Candidate.query.filter_by(is_deleted=False).order_by(Candidate.created_at.desc()).all()
    return render_template('candidates/candidate_list.html', candidates=candidates)

@candidate_views_bp.route('/candidates/<int:candidate_id>', methods=['GET'])
def candidate_profile_page(candidate_id):
    candidate = Candidate.query.get_or_404(candidate_id)
    return render_template('candidates/candidate_profile.html', candidate=candidate)
