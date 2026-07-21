from typing import Generic, Type, TypeVar

from pydantic import BaseModel

ModelType = TypeVar("ModelType")
RepositoryType = TypeVar("RepositoryType")


class BaseService(Generic[ModelType, RepositoryType]):
    def __init__(self, repository: RepositoryType, model: Type[ModelType]):
        self.repository = repository
        self.model = model

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, obj_id: int):
        return self.repository.get(obj_id)

    def create(self, schema: BaseModel):
        obj = self.model(**schema.model_dump())
        return self.repository.create(obj)

    def update(self, obj_id: int, schema: BaseModel):
        obj = self.repository.get(obj_id)

        if not obj:
            return None

        data = schema.model_dump(exclude_unset=True)

        for key, value in data.items():
            setattr(obj, key, value)

        return self.repository.update(obj)

    def delete(self, obj_id: int):
        obj = self.repository.get(obj_id)

        if not obj:
            return False

        self.repository.delete(obj)
        return True