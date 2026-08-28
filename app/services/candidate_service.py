from datetime import datetime
from app.extensions import db
from app.candidates.models import (
    Candidate, CandidateSkill, Experience, Education, 
    CandidateCertification, CandidateProject, CandidateTag, CandidateNote, CandidateActivity
)
from app.skills.service import SkillNormalizationEngine
from app.events.bus import EventBus, EVENT_CANDIDATE_PROFILE_UPDATED
from app.common.errors import APIError

class CandidateService:
    """Enterprise service managing candidate profile intelligence, skill curation, and activity tracking."""

    @classmethod
    def get_or_create_profile(cls, user_id: int, initial_data: dict = None) -> Candidate:
        candidate = Candidate.query.filter_by(user_id=user_id).first()
        if not candidate:
            initial_data = initial_data or {}
            candidate = Candidate(
                user_id=user_id,
                first_name=initial_data.get('first_name', ''),
                last_name=initial_data.get('last_name', ''),
                email=initial_data.get('email', ''),
                headline=initial_data.get('headline', ''),
                phone=initial_data.get('phone'),
                location=initial_data.get('location')
            )
            db.session.add(candidate)
            db.session.commit()
            
            # Log activity
            cls.log_activity(candidate.id, 'PROFILE_CREATED', 'Candidate profile initialized.')
        return candidate

    @classmethod
    def update_profile(cls, candidate_id: int, update_data: dict, actor_id: int = None) -> Candidate:
        candidate = Candidate.query.get_or_404(candidate_id)
        
        allowed_fields = [
            'first_name', 'last_name', 'phone', 'headline', 'summary', 
            'location', 'country', 'city', 'postal_code', 'years_of_experience',
            'highest_education_level', 'linkedin_url', 'github_url', 'portfolio_url', 'website_url'
        ]
        
        for field in allowed_fields:
            if field in update_data:
                setattr(candidate, field, update_data[field])
                
        # Handle Skills list
        if 'skills' in update_data and isinstance(update_data['skills'], list):
            existing_skills = {s.skill_name.lower(): s for s in candidate.skills}
            for sk in update_data['skills']:
                canonical_name = SkillNormalizationEngine.normalize_skill(sk.get('skill_name', ''))
                if canonical_name:
                    if canonical_name.lower() in existing_skills:
                        existing = existing_skills[canonical_name.lower()]
                        existing.years_of_experience = sk.get('years_of_experience', existing.years_of_experience)
                        existing.proficiency = sk.get('proficiency', existing.proficiency)
                    else:
                        new_skill = CandidateSkill(
                            candidate_id=candidate.id,
                            skill_name=canonical_name,
                            years_of_experience=sk.get('years_of_experience', 1.0),
                            proficiency=sk.get('proficiency', 'INTERMEDIATE')
                        )
                        db.session.add(new_skill)

        db.session.commit()
        
        cls.log_activity(candidate.id, 'PROFILE_UPDATED', 'Candidate profile details updated.', actor_id=actor_id)
        
        EventBus.publish(
            event_name=EVENT_CANDIDATE_PROFILE_UPDATED,
            entity_type='Candidate',
            entity_id=candidate.id,
            actor_user_id=actor_id,
            payload={"candidate_id": candidate.id}
        )
        return candidate

    @classmethod
    def add_note(cls, candidate_id: int, author_id: int, note_text: str, is_private: bool = False) -> CandidateNote:
        if not note_text or len(note_text.strip()) == 0:
            raise APIError("Note content cannot be empty", status_code=400)
            
        note = CandidateNote(
            candidate_id=candidate_id,
            author_id=author_id,
            note=note_text,
            is_private=is_private
        )
        db.session.add(note)
        db.session.commit()
        cls.log_activity(candidate_id, 'NOTE_ADDED', f"Recruiter note added.", actor_id=author_id)
        return note

    @classmethod
    def add_tag(cls, candidate_id: int, tag_name: str, actor_id: int = None) -> CandidateTag:
        cleaned_tag = tag_name.strip().lower()
        existing = CandidateTag.query.filter_by(candidate_id=candidate_id, tag=cleaned_tag).first()
        if existing:
            return existing
            
        tag = CandidateTag(candidate_id=candidate_id, tag=cleaned_tag, created_by_user_id=actor_id)
        db.session.add(tag)
        db.session.commit()
        return tag

    @classmethod
    def log_activity(cls, candidate_id: int, activity_type: str, description: str, metadata: dict = None, actor_id: int = None):
        activity = CandidateActivity(
            candidate_id=candidate_id,
            actor_id=actor_id,
            activity_type=activity_type,
            description=description,
            metadata_json=metadata or {}
        )
        db.session.add(activity)
        db.session.commit()
