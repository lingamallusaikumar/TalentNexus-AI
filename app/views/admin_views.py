from flask import Blueprint, render_template
from app.users.models import User
from app.audit.models import AuditLog, SecurityLog
from app.ml_registry.models import MLModelRegistry

admin_views_bp = Blueprint('admin_views', __name__)

@admin_views_bp.route('/admin/users', methods=['GET'])
def admin_users_page():
    users = User.query.filter_by(is_deleted=False).all()
    return render_template('admin/users.html', users=users)

@admin_views_bp.route('/admin/audit-logs', methods=['GET'])
def admin_audit_logs_page():
    logs = AuditLog.query.order_by(AuditLog.created_at.desc()).limit(50).all()
    return render_template('admin/audit_logs.html', logs=logs)

@admin_views_bp.route('/admin/ml-models', methods=['GET'])
def admin_ml_models_page():
    models = MLModelRegistry.query.all()
    return render_template('admin/ml_models.html', models=models)
