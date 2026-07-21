from sqlalchemy.orm import Session

from app.models.product import Product
from app.repositories.base_repository import BaseRepository


class ProductRepository(BaseRepository[Product]):
    def __init__(self, db: Session):
        super().__init__(db, Product)