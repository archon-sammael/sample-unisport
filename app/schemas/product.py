from pydantic import BaseModel, Field
from typing import List, Optional


class PriceModel(BaseModel):
    currency: str
    min_price: str
    max_price: str
    recommended_retail_price: str
    discount_percentage: str


class LabelModel(BaseModel):
    id: int
    name: str
    priority: int
    color: str
    background_color: str
    active: bool


class DeliveryModel(BaseModel):
    min_days: int
    max_days: int
    delivery_string: str


class StockModel(BaseModel):
    pk: int
    sku_id: int
    size_id: int
    barcode: str
    order_by: int
    name: str
    name_short: str
    stock_info: Optional[str] = None
    price: str
    recommended_retail_price: str
    discount_percentage: str
    supplier: str
    is_marketplace: bool
    delivery: DeliveryModel
    availability: str


class AttributesModel(BaseModel):
    club_national: Optional[str] = None
    boot_with_sock: str
    boot_material: str
    boot_model: str
    segment: str
    brand: str
    boot_collection: str
    pricepoint: str
    position: List[str]
    boot_benefit: str
    players: List[str]
    boot_surface: List[str]
    gender: List[str]
    item_type: str
    age: List[str]
    quarter: str
    color: List[str]
    sort_date: str
    brand_collection: str
    warehouse_customization_color: str


class ProductModel(BaseModel):
    id: str
    product_id: int
    style: str
    prices: PriceModel
    name: str
    brand: str
    relative_url: str
    image: str
    delivery: str
    online: bool
    active: bool
    labels: List[LabelModel] = []
    is_customizable: bool
    paid_print: bool
    is_exclusive: bool
    stock: List[StockModel]
    currency: str
    url: str
    attributes: AttributesModel


class ProductListModel(BaseModel):
    products: List[ProductModel]
