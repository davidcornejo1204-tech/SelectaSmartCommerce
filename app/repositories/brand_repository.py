from sqlalchemy.orm import Session

from app.models.brand import Brand
from app.repositories.base_repository import BaseRepository


class BrandRepository(BaseRepository[Brand]):
    def __init__(self, db: Session):
        super().__init__(db, Brand)