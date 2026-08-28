from datetime import datetime
import secrets
import hmac
import hashlib
import json
import urllib.request
import logging
from app.common.models import BaseModel
from app.extensions import db

logger = logging.getLogger(__name__)

class ApiKey(BaseModel):
    __tablename__ = 'api_keys'

    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id', ondelete='CASCADE'), nullable=False, index=True)
    name = db.Column(db.String(128), nullable=False)
    key_prefix = db.Column(db.String(16), nullable=False, index=True) # e.g. tn_live_abc1
    hashed_secret = db.Column(db.String(256), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    expires_at = db.Column(db.DateTime, nullable=True)
    last_used_at = db.Column(db.DateTime, nullable=True)

class WebhookEndpoint(BaseModel):
    __tablename__ = 'webhook_endpoints'

    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id', ondelete='CASCADE'), nullable=False, index=True)
    target_url = db.Column(db.String(512), nullable=False)
    secret_key = db.Column(db.String(128), default=lambda: secrets.token_hex(32))
    subscribed_events = db.Column(db.JSON, default=list) # ["candidate.score.updated", "interview.scheduled"]
    is_active = db.Column(db.Boolean, default=True)

class WebhookDelivery(BaseModel):
    __tablename__ = 'webhook_deliveries'

    webhook_id = db.Column(db.Integer, db.ForeignKey('webhook_endpoints.id', ondelete='CASCADE'), nullable=False, index=True)
    event_name = db.Column(db.String(128), nullable=False)
    payload = db.Column(db.JSON, nullable=False)
    status_code = db.Column(db.Integer, nullable=True)
    response_body = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(32), default='SUCCESS') # SUCCESS, FAILED, RETRYING
    attempt_count = db.Column(db.Integer, default=1)

def dispatch_webhook(webhook_id: int, event_name: str, payload: dict):
    endpoint = WebhookEndpoint.query.get(webhook_id)
    if not endpoint or not endpoint.is_active:
        return
        
    payload_str = json.dumps(payload)
    signature = hmac.new(endpoint.secret_key.encode('utf-8'), payload_str.encode('utf-8'), hashlib.sha256).hexdigest()
    
    headers = {
        'Content-Type': 'application/json',
        'X-TalentNexus-Event': event_name,
        'X-TalentNexus-Signature': signature
    }
    
    req = urllib.request.Request(endpoint.target_url, data=payload_str.encode('utf-8'), headers=headers, method='POST')
    
    delivery = WebhookDelivery(
        webhook_id=endpoint.id,
        event_name=event_name,
        payload=payload
    )
    
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            delivery.status_code = response.getcode()
            delivery.response_body = response.read().decode('utf-8')[:500]
            delivery.status = 'SUCCESS'
    except Exception as e:
        logger.error(f"Webhook delivery failed for endpoint {webhook_id}: {e}")
        delivery.status = 'FAILED'
        delivery.response_body = str(e)
        
    db.session.add(delivery)
    db.session.commit()
