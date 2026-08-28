import os
from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
from app.auth.utils import token_required
from app.extensions import db
from app.resumes.models import Resume, ResumeProcessingJob
from app.resumes.tasks import parse_resume_task
from app.common.errors import APIError

resumes_bp = Blueprint('resumes', __name__)

ALLOWED_EXTENSIONS = {'pdf', 'docx', 'txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@resumes_bp.route('/upload', methods=['POST'])
@token_required
def upload_resume(current_user):
    if not current_user.candidate_profile:
        raise APIError("User does not have a candidate profile", status_code=400)
        
    if 'file' not in request.files:
        raise APIError("No file part provided", status_code=400)
        
    file = request.files['file']
    if file.filename == '':
        raise APIError("No selected file", status_code=400)
        
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_ext = filename.rsplit('.', 1)[1].lower()
        
        # Ensure upload dir exists
        upload_folder = os.path.join(current_app.root_path, '..', 'uploads')
        os.makedirs(upload_folder, exist_ok=True)
        
        file_path = os.path.join(upload_folder, f"{current_user.id}_{filename}")
        file.save(file_path)
        
        # Create database records
        resume = Resume(
            candidate_id=current_user.candidate_profile.id,
            file_name=filename,
            file_path=file_path,
            file_type=file_ext,
            file_size_bytes=os.path.getsize(file_path)
        )
        db.session.add(resume)
        db.session.commit()
        
        processing_job = ResumeProcessingJob(
            resume_id=resume.id,
            status='Queued'
        )
        db.session.add(processing_job)
        db.session.commit()
        
        # Trigger Celery Task
        task = parse_resume_task.delay(resume.id, processing_job.id)
        
        processing_job.celery_task_id = task.id
        db.session.commit()
        
        return jsonify({
            'message': 'Resume uploaded and queued for processing',
            'resume_id': resume.id,
            'job_id': processing_job.id
        }), 202
        
    raise APIError("Invalid file type", status_code=400)
