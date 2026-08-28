from app.common.models import BaseModel
from app.extensions import db

class Organization(BaseModel):
    __tablename__ = 'organizations'

    name = db.Column(db.String(128), nullable=False)
    domain = db.Column(db.String(128), unique=True, nullable=True)
    is_active = db.Column(db.Boolean, default=True)

    users = db.relationship('User', backref='organization', lazy=True)

    def __repr__(self):
        return f"<Organization {self.name}>"
