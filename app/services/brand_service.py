from sqlalchemy.orm import Session

from app.models.brand import Brand
from app.repositories.brand_repository import BrandRepository
from app.services.base_service import BaseService


class BrandService(BaseService[Brand, BrandRepository]):
    def __init__(self, db: Session):
        super().__init__(
            BrandRepository(db),
            Brand,
        )