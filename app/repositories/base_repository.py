from typing import Generic, Type, TypeVar

from sqlalchemy import select
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):
    def __init__(self, db: Session, model: Type[ModelType]):
        self.db = db
        self.model = model

    def get(self, id: int) -> ModelType | None:
        return self.db.get(self.model, id)

    def get_all(self) -> list[ModelType]:
        stmt = select(self.model)
        result = self.db.execute(stmt)
        return list(result.scalars())

    def create(self, obj: ModelType) -> ModelType:
        try:
            self.db.add(obj)
            self.db.commit()
            self.db.refresh(obj)
            return obj
        except Exception:
            self.db.rollback()
            import traceback
            traceback.print_exc()
            raise

    def update(self, obj: ModelType) -> ModelType:
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def delete(self, obj: ModelType) -> None:
        self.db.delete(obj)
        self.db.commit()