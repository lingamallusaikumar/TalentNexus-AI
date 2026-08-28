from flask import Blueprint, render_template

auth_views_bp = Blueprint('auth_views', __name__)

@auth_views_bp.route('/login', methods=['GET'])
def login_page():
    return render_template('auth/login.html')

@auth_views_bp.route('/register', methods=['GET'])
def register_page():
    return render_template('auth/register.html')
