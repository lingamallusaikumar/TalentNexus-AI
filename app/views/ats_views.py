from flask import Blueprint, render_template
from app.applications.models import Application
from app.jobs.models import Job

ats_views_bp = Blueprint('ats_views', __name__)

@ats_views_bp.route('/ats/kanban', methods=['GET'])
def kanban_board_page():
    applications = Application.query.filter_by(status='ACTIVE').all()
    return render_template('ats/kanban.html', applications=applications)
