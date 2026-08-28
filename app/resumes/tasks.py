from datetime import datetime
import logging
from app.extensions import celery, db
from app.resumes.models import Resume, ResumeProcessingJob
from app.resumes.parser import parse_resume_file
from ml.nlp.extractor import clean_text
from ml.resume_parser.section_detector import ResumeSectionDetector
from ml.resume_parser.structured_extractor import StructuredResumeExtractor
from ml.quality_analysis.analyzer import ResumeQualityAnalyzer
from app.skills.service import SkillNormalizationEngine
from app.candidates.models import Candidate, CandidateSkill, CandidateActivity
from app.events.bus import EventBus, EVENT_RESUME_PARSED

logger = logging.getLogger(__name__)

@celery.task(bind=True, name="parse_resume_task")
def parse_resume_task(self, resume_id, processing_job_id):
    logger.info(f"Starting parsing task for resume {resume_id}")
    
    resume = Resume.query.get(resume_id)
    job = ResumeProcessingJob.query.get(processing_job_id)
    
    if not resume or not job:
        logger.error("Resume or ProcessingJob not found.")
        return
        
    try:
        job.status = 'Processing'
        job.started_at = datetime.utcnow()
        db.session.commit()
        
        # 1. Extract and clean raw text
        raw_text = parse_resume_file(resume.file_path, resume.file_type)
        cleaned_text = clean_text(raw_text)
        
        # 2. Section detection & Structured entity extraction
        sections = ResumeSectionDetector.detect_sections(cleaned_text)
        contacts = StructuredResumeExtractor.extract_contact_info(cleaned_text)
        extracted_skills = SkillNormalizationEngine.extract_skills_from_text(cleaned_text)
        quality_report = ResumeQualityAnalyzer.analyze(cleaned_text)
        
        # 3. Update Resume Record
        resume.raw_text = cleaned_text
        resume.is_parsed = True
        resume.parsing_status = 'Completed'
        
        # 4. Update Candidate Profile with extracted data
        candidate = resume.candidate
        if candidate:
            if contacts.get('phone') and not candidate.phone:
                candidate.phone = contacts['phone']
            if contacts.get('linkedin_url') and not candidate.linkedin_url:
                candidate.linkedin_url = contacts['linkedin_url']
            if contacts.get('github_url') and not candidate.github_url:
                candidate.github_url = contacts['github_url']
            if sections.get('summary') and not candidate.summary:
                candidate.summary = sections['summary']
                
            candidate.resume_quality_score = quality_report['overall_score']
            candidate.quality_breakdown = quality_report
            candidate.years_of_experience = StructuredResumeExtractor.estimate_years_of_experience(sections.get('experience', ''))
            
            # Sync candidate skills
            existing_skill_names = {s.skill_name.lower() for s in candidate.skills}
            for skill_data in extracted_skills:
                canonical_name = skill_data['skill_name']
                if canonical_name.lower() not in existing_skill_names:
                    cand_skill = CandidateSkill(
                        candidate_id=candidate.id,
                        skill_name=canonical_name,
                        confidence_score=skill_data['confidence'],
                        years_of_experience=1.5
                    )
                    db.session.add(cand_skill)
                    existing_skill_names.add(canonical_name.lower())
                    
            # Log candidate activity
            activity = CandidateActivity(
                candidate_id=candidate.id,
                activity_type='RESUME_PARSED',
                description=f"Resume '{resume.file_name}' parsed. Quality score: {quality_report['overall_score']}/100."
            )
            db.session.add(activity)

        job.status = 'Completed'
        job.completed_at = datetime.utcnow()
        db.session.commit()
        
        # 5. Publish Event to EventBus
        EventBus.publish(
            event_name=EVENT_RESUME_PARSED,
            entity_type='Resume',
            entity_id=resume.id,
            payload={
                "candidate_id": resume.candidate_id,
                "quality_score": quality_report['overall_score'],
                "skills_count": len(extracted_skills)
            }
        )
        
        logger.info(f"Successfully processed resume {resume_id}")
        
    except Exception as e:
        logger.error(f"Error parsing resume {resume_id}: {str(e)}")
        job.status = 'Failed'
        job.completed_at = datetime.utcnow()
        resume.parsing_status = 'Failed'
        resume.parsing_error = str(e)
        db.session.commit()
        raise e
