from flask import Blueprint, render_template
from app.assessments.models import Assessment

assessment_views_bp = Blueprint('assessment_views', __name__)

@assessment_views_bp.route('/assessments', methods=['GET'])
def assessment_list_page():
    assessments = Assessment.query.filter_by(is_active=True).all()
    return render_template('assessments/assessment_list.html', assessments=assessments)

@assessment_views_bp.route('/assessments/<int:assessment_id>/take', methods=['GET'])
def take_assessment_page(assessment_id):
    assessment = Assessment.query.get_or_404(assessment_id)
    return render_template('assessments/take_assessment.html', assessment=assessment)
