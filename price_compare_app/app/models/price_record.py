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
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

    @classmethod
    def from_mongo(cls, data: dict):
        if not data:
            return data
        id = data.pop('_id', None)
        if 'product_id' in data and isinstance(data['product_id'], ObjectId):
            data['product_id'] = str(data['product_id'])
        return cls(**dict(data, id=str(id) if id else None))

    def to_mongo(self):
        data = self.model_dump(by_alias=True, exclude_none=True)
        if '_id' in data and data['_id']:
            data['_id'] = ObjectId(data['_id'])
        if 'product_id' in data and data['product_id']:
            data['product_id'] = ObjectId(data['product_id'])
        return data