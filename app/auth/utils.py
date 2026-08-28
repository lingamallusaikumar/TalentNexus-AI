import jwt
from datetime import datetime, timedelta
from functools import wraps
from flask import request, current_app
from app.users.models import User
from app.common.errors import APIError

def generate_token(user_id, role_name, org_id):
    payload = {
        'exp': datetime.utcnow() + timedelta(days=1),
        'iat': datetime.utcnow(),
        'sub': user_id,
        'role': role_name,
        'org_id': org_id
    }
    return jwt.encode(payload, current_app.config.get('SECRET_KEY'), algorithm='HS256')

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header.startswith('Bearer '):
                token = auth_header.split(" ")[1]
        
        if not token:
            raise APIError('Token is missing', status_code=401)
            
        try:
            data = jwt.decode(token, current_app.config.get('SECRET_KEY'), algorithms=['HS256'])
            current_user = User.query.get(data['sub'])
            if not current_user:
                raise APIError('User not found', status_code=401)
        except jwt.ExpiredSignatureError:
            raise APIError('Token has expired', status_code=401)
        except jwt.InvalidTokenError:
            raise APIError('Invalid token', status_code=401)
            
        return f(current_user, *args, **kwargs)
    return decorated

def require_role(roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(current_user, *args, **kwargs):
            if current_user.role.name not in roles:
                raise APIError('Insufficient permissions', status_code=403)
            return f(current_user, *args, **kwargs)
        return decorated_function
    return decorator
