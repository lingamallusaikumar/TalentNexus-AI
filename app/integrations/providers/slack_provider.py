import json
import urllib.request
import logging

logger = logging.getLogger(__name__)

class SlackNotificationProvider:
    """Slack Block Kit interactive notification dispatcher for recruitment alerts."""

    @classmethod
    def send_candidate_match_alert(cls, webhook_url: str, candidate_name: str, job_title: str, match_score: float, recommendation: str, dossier_url: str):
        if not webhook_url: return
        
        color = "#10B981" if match_score >= 80 else ("#F59E0B" if match_score >= 60 else "#EF4444")
        payload = {
            "blocks": [
                {
                    "type": "header",
                    "text": {"type": "plain_text", "text": "🎯 New High-Score Candidate Match Detected"}
                },
                {
                    "type": "section",
                    "fields": [
                        {"type": "mrkdwn", "text": f"*Candidate:*\n{candidate_name}"},
                        {"type": "mrkdwn", "text": f"*Target Role:*\n{job_title}"},
                        {"type": "mrkdwn", "text": f"*Match Score:*\n{match_score}%"},
                        {"type": "mrkdwn", "text": f"*AI Recommendation:*\n`{recommendation}`"}
                    ]
                },
                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "button",
                            "text": {"type": "plain_text", "text": "View Candidate Dossier"},
                            "style": "primary",
                            "url": dossier_url
                        }
                    ]
                }
            ]
        }
        cls._post(webhook_url, payload)

    @classmethod
    def send_interview_reminder(cls, webhook_url: str, interviewer_name: str, candidate_name: str, scheduled_time: str, meeting_link: str):
        payload = {
            "blocks": [
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": f"⏰ *Upcoming Interview Reminder for {interviewer_name}*\nCandidate: *{candidate_name}*\nTime: *{scheduled_time}*"}
                }
            ]
        }
        cls._post(webhook_url, payload)

    @classmethod
    def _post(cls, url: str, payload: dict):
        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json'})
            with urllib.request.urlopen(req, timeout=5) as resp:
                pass
        except Exception as e:
            logger.error(f"Slack webhook delivery failed: {e}")
