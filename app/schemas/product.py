from typing import List, Optional

from pydantic import BaseModel, Field


class Product(BaseModel):
    sku: str
    name: str
    category: str
    mrp: float
    distributor_price: float
    retailer_margin_percent: float
    moq: int = Field(description="Minimum order quantity")
    shelf_life_days: int
    benefits: List[str]
    offers: Optional[List[str]] = None
    source: str = "manual"


class ProductBatch(BaseModel):
    products: List[Product]
