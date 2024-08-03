# app/models/price_record.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from bson import ObjectId

class PriceRecordModel(BaseModel):
    id: Optional[str] = Field(alias="_id", default=None)
    product_id: str
    product_name: str
    price: float
    unit: str
    store: str
    date: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True
        json_encoders = {ObjectId: str}

    @classmethod
    def from_mongo(cls, data: dict):
        if not data:
            return None
        mongo_id = data.pop('_id', None)
        if mongo_id:
            data['id'] = str(mongo_id)
        if 'product_id' in data and isinstance(data['product_id'], ObjectId):
            data['product_id'] = str(data['product_id'])
        return cls(**data)