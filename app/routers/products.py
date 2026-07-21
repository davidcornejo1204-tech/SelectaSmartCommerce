from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.product import (
    ProductCreate,
    ProductUpdate,
    ProductResponse,
)
from app.services.product_service import ProductService

router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


@router.get("/", response_model=List[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return ProductService(db).get_all()


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = ProductService(db).get_by_id(product_id)

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    return product


@router.post("/", response_model=ProductResponse)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
):
    return ProductService(db).create(product)


@router.put("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    product: ProductUpdate,
    db: Session = Depends(get_db),
):
    updated = ProductService(db).update(product_id, product)

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    return updated


@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
):
    deleted = ProductService(db).delete(product_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    return {"message": "Product deleted"}