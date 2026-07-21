from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.category import (
    CategoryCreate,
    CategoryUpdate,
    CategoryResponse,
)
from app.services.category_service import CategoryService

router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)


@router.get("/", response_model=List[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return CategoryService(db).get_all()


@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = CategoryService(db).get_by_id(category_id)

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    return category


@router.post("/", response_model=CategoryResponse)
def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db),
):
    return CategoryService(db).create(category)


@router.put("/{category_id}", response_model=CategoryResponse)
def update_category(
    category_id: int,
    category: CategoryUpdate,
    db: Session = Depends(get_db),
):
    updated = CategoryService(db).update(category_id, category)

    if not updated:
        raise HTTPException(status_code=404, detail="Category not found")

    return updated


@router.delete("/{category_id}")
def delete_category(
    category_id: int,
    db: Session = Depends(get_db),
):
    deleted = CategoryService(db).delete(category_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Category not found")

    return {"message": "Category deleted"}