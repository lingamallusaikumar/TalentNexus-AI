from flask import Blueprint, request, jsonify
from app.extensions import db
from app.users.models import User, Role
from app.organizations.models import Organization
from app.auth.utils import generate_token, token_required
from app.common.errors import APIError

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('password'):
        raise APIError('Missing required fields', status_code=400)
        
    if User.query.filter_by(email=data['email']).first():
        raise APIError('Email already registered', status_code=400)
        
    # Get or create default role (for MVP phase 2)
    role_name = data.get('role', 'Candidate')
    role = Role.query.filter_by(name=role_name).first()
    if not role:
        role = Role(name=role_name)
        db.session.add(role)
        db.session.commit()
        
    # Handle org setup if organization provided
    org_id = None
    if data.get('organization_name'):
        org = Organization(name=data['organization_name'])
        db.session.add(org)
        db.session.commit()
        org_id = org.id
        
    user = User(
        email=data['email'],
        first_name=data.get('first_name', ''),
        last_name=data.get('last_name', ''),
        password=data['password'],
        role_id=role.id,
        organization_id=org_id
    )
    
    user.save()
    
    token = generate_token(user.id, role.name, org_id)
    
    return jsonify({
        'message': 'User registered successfully',
        'token': token
    }), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('password'):
        raise APIError('Missing required fields', status_code=400)
        
    user = User.query.filter_by(email=data['email']).first()
    
    if not user or not user.verify_password(data['password']):
        raise APIError('Invalid email or password', status_code=401)
        
    if not user.is_active:
        raise APIError('Account is disabled', status_code=401)
        
    token = generate_token(user.id, user.role.name, user.organization_id)
    
    return jsonify({
        'token': token,
        'user': {
            'id': user.id,
            'email': user.email,
            'role': user.role.name,
            'organization_id': user.organization_id
        }
    }), 200

@auth_bp.route('/me', methods=['GET'])
@token_required
def get_current_user(current_user):
    return jsonify({
        'id': current_user.id,
        'email': current_user.email,
        'first_name': current_user.first_name,
        'last_name': current_user.last_name,
        'role': current_user.role.name,
        'organization_id': current_user.organization_id
    }), 200
