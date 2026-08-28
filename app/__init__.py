import os
from flask import Flask
from app.config import config_by_name
from app.extensions import db, migrate, celery, init_celery, ma

def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'dev')
        
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    
    init_celery(app, celery)
    
    from app.realtime.socketio import socketio
    
    # Use config URL if available
    redis_url = app.config.get('REDIS_URL', 'redis://localhost:6379/0')
    socketio.init_app(app, message_queue=redis_url)
    
    # Register blueprints
    from app.api import api_bp
    from app.auth.routes import auth_bp
    from app.resumes.routes import resumes_bp
    
    app.register_blueprint(api_bp, url_prefix='/api/v1')
    app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
    app.register_blueprint(resumes_bp, url_prefix='/api/v1/resumes')
    
    # Register error handlers and logger
    from app.common.errors import register_error_handlers
    from app.common.logger import setup_logger
    
    register_error_handlers(app)
    setup_logger(app)
    
    # Health check endpoint at root level as well
    @app.route('/health')
    def health():
        return {'status': 'healthy', 'service': 'talentnexus-ai'}
        
    return app
