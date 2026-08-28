from flask import Blueprint, render_template
from app.jobs.models import Job

job_views_bp = Blueprint('job_views', __name__)

@job_views_bp.route('/jobs', methods=['GET'])
def list_jobs_page():
    jobs = Job.query.filter_by(is_deleted=False).order_by(Job.created_at.desc()).all()
    return render_template('jobs/job_list.html', jobs=jobs)

@job_views_bp.route('/jobs/new', methods=['GET'])
def create_job_page():
    return render_template('jobs/job_create.html')

@job_views_bp.route('/jobs/<int:job_id>', methods=['GET'])
def job_detail_page(job_id):
    job = Job.query.get_or_404(job_id)
    return render_template('jobs/job_detail.html', job=job)
