from sqlalchemy.orm import Session

from app.models.category import Category
from app.repositories.category_repository import CategoryRepository
from app.services.base_service import BaseService


class CategoryService(BaseService[Category, CategoryRepository]):
    def __init__(self, db: Session):
        super().__init__(
            CategoryRepository(db),
            Category,
        )