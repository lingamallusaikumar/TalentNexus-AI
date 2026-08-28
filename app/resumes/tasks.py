from datetime import datetime
from app.extensions import celery, db
from app.resumes.models import Resume, ResumeProcessingJob
from app.resumes.parser import parse_resume_file
from ml.nlp.extractor import clean_text, extract_entities
import logging

logger = logging.getLogger(__name__)

@celery.task(bind=True, name="parse_resume_task")
def parse_resume_task(self, resume_id, processing_job_id):
    logger.info(f"Starting parsing task for resume {resume_id}")
    
    # We must fetch instances freshly inside the task context
    resume = Resume.query.get(resume_id)
    job = ResumeProcessingJob.query.get(processing_job_id)
    
    if not resume or not job:
        logger.error("Resume or ProcessingJob not found.")
        return
        
    try:
        job.status = 'Processing'
        job.started_at = datetime.utcnow()
        db.session.commit()
        
        # 1. Extract text from file
        raw_text = parse_resume_file(resume.file_path, resume.file_type)
        cleaned_text = clean_text(raw_text)
        
        # 2. Update resume
        resume.raw_text = cleaned_text
        resume.is_parsed = True
        resume.parsing_status = 'Completed'
        
        # 3. Future step: extract structured data (skills, exp) using ml.nlp here
        # entities = extract_entities(cleaned_text)
        
        job.status = 'Completed'
        job.completed_at = datetime.utcnow()
        db.session.commit()
        logger.info(f"Successfully parsed resume {resume_id}")
        
    except Exception as e:
        logger.error(f"Error parsing resume {resume_id}: {str(e)}")
        job.status = 'Failed'
        job.completed_at = datetime.utcnow()
        resume.parsing_status = 'Failed'
        resume.parsing_error = str(e)
        db.session.commit()
        raise e
