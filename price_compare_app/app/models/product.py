# app/models/product.py
from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class ProductModel(BaseModel):
    id: Optional[str] = Field(alias="_id", default=None)
    name: str
    category: str
    brand: Optional[str] = None

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

    @classmethod
    def from_mongo(cls, data: dict):
        """We must convert _id from ObjectId to str"""
        if not data:
            return data
        id = data.pop('_id', None)
        return cls(**dict(data, id=str(id) if id else None))

    def to_mongo(self):
        """Convert id to ObjectId"""
        data = self.model_dump(by_alias=True, exclude_none=True)
        if data.get("_id"):
            data["_id"] = ObjectId(data["_id"])
        return data