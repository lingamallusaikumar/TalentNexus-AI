import logging
from flask import render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

logger = logging.getLogger(__name__)

class EmailDeliveryService:
    """Enterprise transactional email delivery service."""

    @classmethod
    def send_interview_invitation(cls, candidate_email: str, candidate_name: str, job_title: str, scheduled_time: str, meeting_link: str = None):
        subject = f"Interview Scheduled: {job_title} at TalentNexus"
        body = f"""
        Hello {candidate_name},

        You have an interview scheduled for the position of {job_title}.

        📅 Date & Time: {scheduled_time}
        🔗 Meeting Link: {meeting_link or 'Details to follow'}

        Please arrive 5 minutes early.

        Best regards,
        Talent Acquisition Team
        """
        cls._send_email(candidate_email, subject, body)

    @classmethod
    def send_application_status_update(cls, candidate_email: str, candidate_name: str, job_title: str, new_stage: str):
        subject = f"Update on your application for {job_title}"
        body = f"""
        Hello {candidate_name},

        Your application for {job_title} has been moved to the '{new_stage}' stage.
        Our recruitment team will contact you with next steps.

        Best regards,
        Recruitment Team
        """
        cls._send_email(candidate_email, subject, body)

    @classmethod
    def _send_email(cls, recipient: str, subject: str, body: str):
        try:
            logger.info(f"📧 [Email Mock Service] Dispatched email to {recipient} with subject '{subject}'.")
        except Exception as e:
            logger.error(f"Failed to send email to {recipient}: {e}")
