from decimal import Decimal

from sqlalchemy import (
    Boolean,
    ForeignKey,
    Numeric,
    String,
    Text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.base import Base, TimestampMixin


class Product(Base, TimestampMixin):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)

    # Identificación
    sku: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True,
    )

    barcode: Mapped[str | None] = mapped_column(
        String(50),
        unique=True,
        nullable=True,
        index=True,
    )

    invima: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    # Información comercial
    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
        index=True,
    )

    generic_name: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    presentation: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # Relaciones
    brand_id: Mapped[int] = mapped_column(
        ForeignKey("brands.id"),
        nullable=False,
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"),
        nullable=False,
    )

    brand = relationship("Brand")
    category = relationship("Category")

    # Inventario
    stock: Mapped[int] = mapped_column(
        default=0,
        nullable=False,
    )

    stock_min: Mapped[int] = mapped_column(
        default=0,
        nullable=False,
    )

    stock_max: Mapped[int] = mapped_column(
        default=0,
        nullable=False,
    )

    # Precios
    cost_price: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        default=0,
    )

    sale_price: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        default=0,
    )

    tax_rate: Mapped[Decimal] = mapped_column(
        Numeric(5, 2),
        default=0,
    )

    # Configuración
    active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    requires_prescription: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    is_featured: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    # Integraciones
    image_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    woocommerce_id: Mapped[int | None] = mapped_column(
        nullable=True,
    )

    mercadolibre_id: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    dominium_id: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )