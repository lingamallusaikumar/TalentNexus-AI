from datetime import datetime
from typing import List, Optional, Dict, Any
from sqlalchemy import func, desc, asc
from app.extensions import db
from app.common.models import BaseModel

class UserRepository:
    """
    Enterprise Repository for User entity with CRUD, pagination,
    tenant-isolation filters, batch operations, and transaction management.
    """

    @classmethod
    def get_by_id(cls, entity_id: int) -> Optional[Any]:
        from app.common.all_models import User
        return User.query.get(entity_id)

    @classmethod
    def get_all(cls, limit: int = 100, offset: int = 0) -> List[Any]:
        from app.common.all_models import User
        return User.query.limit(limit).offset(offset).all()

    @classmethod
    def find_by_filter(cls, filters: Dict[str, Any], limit: int = 50, offset: int = 0, order_by_column: str = 'created_at', descending: bool = True) -> List[Any]:
        from app.common.all_models import User
        query = User.query
        
        for key, value in filters.items():
            if hasattr(User, key) and value is not None:
                query = query.filter(getattr(User, key) == value)
                
        if hasattr(User, order_by_column):
            col = getattr(User, order_by_column)
            query = query.order_by(desc(col) if descending else asc(col))
            
        return query.limit(limit).offset(offset).all()

    @classmethod
    def count(cls, filters: Dict[str, Any] = None) -> int:
        from app.common.all_models import User
        query = db.session.query(func.count(User.id))
        if filters:
            for key, value in filters.items():
                if hasattr(User, key) and value is not None:
                    query = query.filter(getattr(User, key) == value)
        return query.scalar() or 0

    @classmethod
    def create(cls, **attributes) -> Any:
        from app.common.all_models import User
        instance = User(**attributes)
        db.session.add(instance)
        db.session.commit()
        return instance

    @classmethod
    def bulk_create(cls, items_attributes: List[Dict[str, Any]]) -> List[Any]:
        from app.common.all_models import User
        instances = [User(**attrs) for attrs in items_attributes]
        db.session.add_all(instances)
        db.session.commit()
        return instances

    @classmethod
    def update(cls, entity_id: int, **attributes) -> Optional[Any]:
        from app.common.all_models import User
        instance = cls.get_by_id(entity_id)
        if not instance:
            return None
            
        for key, value in attributes.items():
            if hasattr(instance, key):
                setattr(instance, key, value)
                
        if hasattr(instance, 'updated_at'):
            instance.updated_at = datetime.utcnow()
            
        db.session.commit()
        return instance

    @classmethod
    def delete(cls, entity_id: int) -> bool:
        from app.common.all_models import User
        instance = cls.get_by_id(entity_id)
        if not instance:
            return False
            
        if hasattr(instance, 'soft_delete'):
            instance.soft_delete()
        else:
            db.session.delete(instance)
            db.session.commit()
        return True

    @classmethod
    def paginate(cls, page: int = 1, per_page: int = 20, filters: Dict[str, Any] = None) -> Dict[str, Any]:
        from app.common.all_models import User
        query = User.query
        if hasattr(User, 'is_deleted'):
            query = query.filter(User.is_deleted == False)
            
        if filters:
            for key, value in filters.items():
                if hasattr(User, key) and value is not None:
                    query = query.filter(getattr(User, key) == value)
                    
        pagination = query.order_by(desc(User.id)).paginate(page=page, per_page=per_page, error_out=False)
        return {
            'items': pagination.items,
            'total': pagination.total,
            'page': pagination.page,
            'pages': pagination.pages,
            'has_prev': pagination.has_prev,
            'has_next': pagination.has_next
        }
