# app/schemas/product.py
from pydantic import BaseModel, Field
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    category: str
    brand: Optional[str] = None

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    brand: Optional[str] = None

class ProductInDB(ProductCreate):
    id: str = Field(alias="_id")

    class Config:
        populate_by_name = True