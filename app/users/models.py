from app.common.models import BaseModel
from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class Role(BaseModel):
    __tablename__ = 'roles'
    
    name = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    
    users = db.relationship('User', backref='role', lazy=True)

class User(BaseModel):
    __tablename__ = 'users'

    email = db.Column(db.String(128), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    
    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id'), nullable=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.email}>"
