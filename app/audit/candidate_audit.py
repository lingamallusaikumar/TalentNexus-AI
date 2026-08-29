import logging
from datetime import datetime
from typing import Optional

logger = logging.getLogger("talentnexus.audit")

def log_candidate_access(user_id: str, candidate_id: str, action: str, ip_address: Optional[str] = None):
    """Logs access to candidate PII records for GDPR / compliance auditing."""
    audit_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "user_id": user_id,
        "candidate_id": candidate_id,
        "action": action,
        "ip_address": ip_address or "unknown"
    }
    logger.info(f"AUDIT_EVENT: {audit_entry}")
    return audit_entry
