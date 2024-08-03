# app/models/product.py
from pydantic import BaseModel, Field
from typing import Optional, Any
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v: Any) -> ObjectId:
        if not isinstance(v, ObjectId):
            if not ObjectId.is_valid(v):
                raise ValueError("Invalid objectid")
            v = ObjectId(v)
        return v

    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema):
        field_schema.update(type="string")

class ProductModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    category: str
    brand: Optional[str] = None

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        
    def model_dump(self, **kwargs):
        if 'exclude' in kwargs:
            kwargs['exclude'] = set(kwargs['exclude']) | {'id'}
        else:
            kwargs['exclude'] = {'id'}
        data = super().model_dump(**kwargs)
        if '_id' in data:
            data['id'] = str(data['_id'])
        return data