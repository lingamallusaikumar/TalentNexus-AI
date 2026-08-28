from datetime import datetime
from app.extensions import db
from sqlalchemy import Column, Integer, DateTime, Boolean, String, ForeignKey
from sqlalchemy.orm import declared_attr

class BaseModel(db.Model):
    __abstract__ = True
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class TenantAwareMixin:
    """Mixin for multi-tenant data isolation across organizations."""
    @declared_attr
    def organization_id(cls):
        return db.Column(db.Integer, db.ForeignKey('organizations.id', ondelete='CASCADE'), nullable=False, index=True)

class SoftDeleteMixin:
    """Mixin for soft-deleting entities while preserving historical audit trails."""
    is_deleted = db.Column(db.Boolean, default=False, nullable=False, index=True)
    deleted_at = db.Column(db.DateTime, nullable=True)

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = datetime.utcnow()
        db.session.commit()

    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        db.session.commit()
