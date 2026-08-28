from flask import Blueprint, jsonify
from app.extensions import db

api_bp = Blueprint('api', __name__)

@api_bp.route('/health', methods=['GET'])
def health_check():
    health_status = {
        "status": "healthy",
        "database": "unknown"
    }
    try:
        db.session.execute(db.text('SELECT 1'))
        health_status["database"] = "healthy"
    except Exception as e:
        health_status["database"] = "unhealthy"
        health_status["status"] = "unhealthy"
        
    return jsonify(health_status), 200 if health_status["status"] == "healthy" else 503
