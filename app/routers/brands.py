from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.brand import (
    BrandCreate,
    BrandUpdate,
    BrandResponse,
)
from app.services.brand_service import BrandService

router = APIRouter(
    prefix="/brands",
    tags=["Brands"],
)


@router.get("/", response_model=List[BrandResponse])
def get_brands(db: Session = Depends(get_db)):
    return BrandService(db).get_all()


@router.get("/{brand_id}", response_model=BrandResponse)
def get_brand(brand_id: int, db: Session = Depends(get_db)):
    brand = BrandService(db).get_by_id(brand_id)

    if not brand:
        raise HTTPException(404, "Brand not found")

    return brand


@router.post("/", response_model=BrandResponse)
def create_brand(
    brand: BrandCreate,
    db: Session = Depends(get_db),
):
    return BrandService(db).create(brand)


@router.put("/{brand_id}", response_model=BrandResponse)
def update_brand(
    brand_id: int,
    brand: BrandUpdate,
    db: Session = Depends(get_db),
):
    updated = BrandService(db).update(brand_id, brand)

    if not updated:
        raise HTTPException(404, "Brand not found")

    return updated


@router.delete("/{brand_id}")
def delete_brand(
    brand_id: int,
    db: Session = Depends(get_db),
):
    deleted = BrandService(db).delete(brand_id)

    if not deleted:
        raise HTTPException(404, "Brand not found")

    return {"message": "Brand deleted"}