from flask import Blueprint, jsonify
from app.analytics.services import get_recruitment_funnel_metrics
from app.auth.utils import token_required

analytics_bp = Blueprint('analytics', __name__)

@analytics_bp.route('/funnel', methods=['GET'])
@token_required
def get_funnel_dashboard(current_user):
    org_id = current_user.current_organization_id or 1
    metrics = get_recruitment_funnel_metrics(org_id)
    return jsonify(metrics), 200
