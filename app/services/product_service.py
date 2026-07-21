from sqlalchemy.orm import Session

from app.models.product import Product
from app.repositories.product_repository import ProductRepository
from app.services.base_service import BaseService


class ProductService(BaseService[Product, ProductRepository]):
    def __init__(self, db: Session):
        super().__init__(
            ProductRepository(db),
            Product,
        )