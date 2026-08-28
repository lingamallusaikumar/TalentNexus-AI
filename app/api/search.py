from flask import Blueprint, request, jsonify
from app.search.services import SemanticSearchEngine
from app.recommendations.services import RecommendationEngine
from app.auth.utils import token_required

search_bp = Blueprint('search', __name__)

@search_bp.route('/candidates', methods=['POST', 'GET'])
@token_required
def semantic_search_candidates(current_user):
    query = request.args.get('q') or (request.get_json() or {}).get('query')
    if not query:
        return jsonify({"results": []}), 200
        
    results = SemanticSearchEngine.search_candidates(query, current_user.current_organization_id)
    return jsonify({
        "query": query,
        "count": len(results),
        "results": results
    }), 200

@search_bp.route('/recommendations/jobs/<int:candidate_id>', methods=['GET'])
@token_required
def recommend_jobs(current_user, candidate_id):
    recs = RecommendationEngine.recommend_jobs_for_candidate(candidate_id)
    return jsonify({"recommendations": recs}), 200

@search_bp.route('/recommendations/similar-candidates/<int:candidate_id>', methods=['GET'])
@token_required
def recommend_similar(current_user, candidate_id):
    similar = RecommendationEngine.recommend_similar_candidates(candidate_id)
    return jsonify({"similar_candidates": similar}), 200
