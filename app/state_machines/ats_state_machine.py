from typing import Dict, List, Optional
import logging

logger = logging.getLogger(__name__)

class ATSStateMachine:
    """
    Finite State Machine (FSM) controlling candidate application lifecycles,
    transition validation, side-effect hooks, and rejection state management.
    """

    TRANSITIONS = {
        'Applied': ['AI Screening', 'Recruiter Review', 'Rejected', 'Withdrawn'],
        'AI Screening': ['Recruiter Review', 'Shortlisted', 'Rejected', 'Withdrawn'],
        'Recruiter Review': ['Shortlisted', 'Assessment', 'Interview', 'Rejected', 'Withdrawn'],
        'Shortlisted': ['Assessment', 'Interview', 'Offer', 'Rejected', 'Withdrawn'],
        'Assessment': ['Interview', 'Shortlisted', 'Rejected', 'Withdrawn'],
        'Interview': ['Panel Interview', 'Offer', 'Rejected', 'Withdrawn'],
        'Panel Interview': ['Executive Review', 'Offer', 'Rejected', 'Withdrawn'],
        'Executive Review': ['Offer', 'Rejected', 'Withdrawn'],
        'Offer': ['Hired', 'Offer Rejected', 'Withdrawn'],
        'Hired': [], # Terminal
        'Rejected': ['Applied'], # Allowed for re-consideration
        'Withdrawn': [] # Terminal
    }

    @classmethod
    def can_transition(cls, from_stage: str, to_stage: str) -> bool:
        allowed = cls.TRANSITIONS.get(from_stage, [])
        return to_stage in allowed

    @classmethod
    def validate_transition(cls, from_stage: str, to_stage: str):
        if not cls.can_transition(from_stage, to_stage):
            raise ValueError(f"Illegal ATS state transition from '{from_stage}' to '{to_stage}'.")
