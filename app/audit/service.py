from flask import request
from app.extensions import db
from app.audit.models import AuditLog, SecurityLog

def log_audit(action: str, resource_type: str, resource_id: int = None, changes: dict = None, organization_id: int = None, user_id: int = None):
    ip_address = None
    user_agent = None
    if request:
        try:
            ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
            user_agent = request.user_agent.string if request.user_agent else None
        except Exception:
            pass

    log = AuditLog(
        organization_id=organization_id,
        user_id=user_id,
        action=action,
        resource_type=resource_type,
        resource_id=resource_id,
        changes=changes,
        ip_address=ip_address,
        user_agent=user_agent
    )
    db.session.add(log)
    db.session.commit()
    return log

def log_security(event_type: str, severity: str = 'INFO', details: dict = None, organization_id: int = None, user_id: int = None):
    ip_address = None
    user_agent = None
    if request:
        try:
            ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
            user_agent = request.user_agent.string if request.user_agent else None
        except Exception:
            pass

    log = SecurityLog(
        organization_id=organization_id,
        user_id=user_id,
        event_type=event_type,
        severity=severity,
        details=details,
        ip_address=ip_address,
        user_agent=user_agent
    )
    db.session.add(log)
    db.session.commit()
    return log
