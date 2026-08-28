import os
from flask import Flask, render_template
from app.config import config_by_name
from app.extensions import db, migrate, celery, init_celery, ma

def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'dev')
        
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.from_object(config_by_name[config_name])
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    
    init_celery(app, celery)
    
    from app.realtime.socketio import socketio
    redis_url = app.config.get('REDIS_URL', 'redis://localhost:6379/0')
    socketio.init_app(app, message_queue=redis_url)
    
    # 1. Register API Blueprints
    from app.api import (
        api_bp, auth_bp, resumes_bp, candidates_bp, 
        jobs_bp, matching_bp, applications_bp, search_bp, analytics_bp
    )
    
    app.register_blueprint(api_bp, url_prefix='/api/v1')
    app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
    app.register_blueprint(resumes_bp, url_prefix='/api/v1/resumes')
    app.register_blueprint(candidates_bp, url_prefix='/api/v1/candidates')
    app.register_blueprint(jobs_bp, url_prefix='/api/v1/jobs')
    app.register_blueprint(matching_bp, url_prefix='/api/v1/matches')
    app.register_blueprint(applications_bp, url_prefix='/api/v1/applications')
    app.register_blueprint(search_bp, url_prefix='/api/v1/search')
    app.register_blueprint(analytics_bp, url_prefix='/api/v1/analytics')

    # 2. Register Web View Blueprints
    from app.views import (
        auth_views_bp, job_views_bp, candidate_views_bp, 
        ats_views_bp, admin_views_bp, assessment_views_bp
    )
    app.register_blueprint(auth_views_bp)
    app.register_blueprint(job_views_bp)
    app.register_blueprint(candidate_views_bp)
    app.register_blueprint(ats_views_bp)
    app.register_blueprint(admin_views_bp)
    app.register_blueprint(assessment_views_bp)
    
    # Register error handlers and logger
    from app.common.errors import register_error_handlers
    from app.common.logger import setup_logger
    
    register_error_handlers(app)
    setup_logger(app)
    
    # Root dashboard UI route
    @app.route('/')
    def index():
        return render_template('dashboard.html')

    @app.route('/health')
    def health():
        return {'status': 'healthy', 'service': 'talentnexus-ai', 'version': '1.0.0'}
        
    return app
