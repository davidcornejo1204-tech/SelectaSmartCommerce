from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    sku: str
    barcode: str | None = None
    invima: str | None = None

    name: str
    generic_name: str | None = None
    presentation: str | None = None
    description: str | None = None

    brand_id: int
    category_id: int

    stock: int = 0
    stock_min: int = 0
    stock_max: int = 0

    cost_price: Decimal = Decimal("0.00")
    sale_price: Decimal = Decimal("0.00")
    tax_rate: Decimal = Decimal("0.00")

    active: bool = True
    requires_prescription: bool = False
    is_featured: bool = False

    image_url: str | None = None

    woocommerce_id: int | None = None
    mercadolibre_id: str | None = None
    dominium_id: str | None = None


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    sku: str | None = None
    barcode: str | None = None
    invima: str | None = None

    name: str | None = None
    generic_name: str | None = None
    presentation: str | None = None
    description: str | None = None

    brand_id: int | None = None
    category_id: int | None = None

    stock: int | None = None
    stock_min: int | None = None
    stock_max: int | None = None

    cost_price: Decimal | None = None
    sale_price: Decimal | None = None
    tax_rate: Decimal | None = None

    active: bool | None = None
    requires_prescription: bool | None = None
    is_featured: bool | None = None

    image_url: str | None = None

    woocommerce_id: int | None = None
    mercadolibre_id: str | None = None
    dominium_id: str | None = None


class ProductResponse(ProductBase):
    id: int

    model_config = ConfigDict(from_attributes=True)