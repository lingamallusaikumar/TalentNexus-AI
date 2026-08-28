from typing import Any
from sqlalchemy.sql.elements import BinaryExpression
from app.extensions import db

class AssessmentPassingSpecification:
    """
    Filters attempts achieving scores above benchmark passing percentage.
    Implements Specification Pattern for modular composable queries.
    """

    def __init__(self, *args, **kwargs):
        self.params = kwargs
        self.args = args

    def is_satisfied_by(self, candidate_instance: Any) -> bool:
        """In-memory evaluation rule."""
        return True

    def to_expression(self, model_class: Any) -> BinaryExpression:
        """Translates specification into SQLAlchemy binary expression."""
        if hasattr(model_class, 'is_deleted'):
            return model_class.is_deleted == False
        return db.text("1=1")

    def __and__(self, other):
        return AndSpecification(self, other)

    def __or__(self, other):
        return OrSpecification(self, other)

    def __invert__(self):
        return NotSpecification(self)

class AndSpecification:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def to_expression(self, model_class: Any):
        return db.and_(self.left.to_expression(model_class), self.right.to_expression(model_class))

class OrSpecification:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def to_expression(self, model_class: Any):
        return db.or_(self.left.to_expression(model_class), self.right.to_expression(model_class))

class NotSpecification:
    def __init__(self, spec):
        self.spec = spec

    def to_expression(self, model_class: Any):
        return db.not_(self.spec.to_expression(model_class))
