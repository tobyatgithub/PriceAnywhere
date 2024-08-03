# app/schemas/price_record.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class PriceRecordCreate(BaseModel):
    product_name: str  # 使用 product_name 替代 product_id
    price: float
    unit: str
    store: str
    date: Optional[datetime] = None

class PriceRecordUpdate(BaseModel):
    price: Optional[float] = None
    unit: Optional[str] = None
    store: Optional[str] = None
    date: Optional[datetime] = None

class PriceRecordInDB(BaseModel):
    id: str = Field(alias="_id")
    product_id: str
    product_name: str
    price: float
    unit: str
    store: str
    date: datetime

    class Config:
        populate_by_name = True