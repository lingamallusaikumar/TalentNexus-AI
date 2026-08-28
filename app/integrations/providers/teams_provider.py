import json
import urllib.request
import logging

logger = logging.getLogger(__name__)

class TeamsNotificationProvider:
    """Microsoft Teams Adaptive Cards notification dispatcher."""

    @classmethod
    def send_card(cls, webhook_url: str, title: str, subtitle: str, facts: list):
        if not webhook_url: return
        card = {
            "type": "message",
            "attachments": [{
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "type": "AdaptiveCard",
                    "version": "1.4",
                    "body": [
                        {"type": "TextBlock", "text": title, "weight": "Bolder", "size": "Medium"},
                        {"type": "TextBlock", "text": subtitle, "isSubtle": True},
                        {"type": "FactSet", "facts": [{"title": f.get('title'), "value": f.get('value')} for f in facts]}
                    ]
                }
            }]
        }
        try:
            req = urllib.request.Request(webhook_url, data=json.dumps(card).encode('utf-8'), headers={'Content-Type': 'application/json'})
            with urllib.request.urlopen(req, timeout=5) as resp:
                pass
        except Exception as e:
            logger.error(f"Teams webhook delivery failed: {e}")
