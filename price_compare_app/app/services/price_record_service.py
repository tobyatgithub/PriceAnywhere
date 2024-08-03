# app/services/price_record_service.py
from app.models.price_record import PriceRecordModel
from app.models.product import ProductModel
from app.database import database
from bson import ObjectId
from app.schemas.price_record import PriceRecordCreate, PriceRecordInDB, PriceRecordUpdate

price_record_collection = database.get_collection("price_records")
product_collection = database.get_collection("products")

class PriceRecordService:
    @staticmethod
    async def create_price_record(price_record: PriceRecordCreate):
        # 查找或创建 product
        product = await product_collection.find_one({"name": price_record.product_name})
        if not product:
            new_product = ProductModel(name=price_record.product_name, category="Unknown")
            result = await product_collection.insert_one(new_product.dict(exclude={"id"}))
            product_id = str(result.inserted_id)
        else:
            product_id = str(product["_id"])

        price_record_dict = price_record.dict()
        price_record_dict["product_id"] = product_id
        result = await price_record_collection.insert_one(price_record_dict)
        created_record = await PriceRecordService.get_price_record(str(result.inserted_id))
        return created_record

    @staticmethod
    async def get_price_record(price_record_id: str):
        price_record = await price_record_collection.find_one({"_id": ObjectId(price_record_id)})
        if price_record:
            product = await product_collection.find_one({"_id": ObjectId(price_record["product_id"])})
            if product:
                price_record["product_name"] = product["name"]
            return PriceRecordModel.from_mongo(price_record)
        return None

    @staticmethod
    async def update_price_record(price_record_id: str, price_record_data: PriceRecordUpdate):
        update_data = price_record_data.dict(exclude_unset=True)
        
        if 'product_name' in update_data:
            # 如果更新包含新的 product_name，我们需要更新或创建对应的 product
            product_name = update_data.pop('product_name')
            product = await product_collection.find_one({"name": product_name})
            if not product:
                new_product = ProductModel(name=product_name, category="Unknown")
                result = await product_collection.insert_one(new_product.dict(exclude={"id"}))
                product_id = result.inserted_id
            else:
                product_id = product["_id"]
            update_data['product_id'] = product_id

        update_result = await price_record_collection.update_one(
            {"_id": ObjectId(price_record_id)}, {"$set": update_data}
        )
        
        if update_result.modified_count > 0:
            # 如果更新成功，返回更新后的记录
            updated_record = await PriceRecordService.get_price_record(price_record_id)
            return updated_record
        return None

    @staticmethod
    async def delete_price_record(price_record_id: str):
        delete_result = await price_record_collection.delete_one({"_id": ObjectId(price_record_id)})
        return delete_result.deleted_count > 0

    @staticmethod
    async def list_price_records(product_name: str = None):
        filter = {}
        if product_name:
            product = await product_collection.find_one({"name": product_name})
            if product:
                filter["product_id"] = product["_id"]
            else:
                return []  # 如果找不到对应的产品，返回空列表

        price_records = []
        async for record in price_record_collection.find(filter):
            product = await product_collection.find_one({"_id": record["product_id"]})
            if product:
                record["product_name"] = product["name"]
            price_records.append(PriceRecordModel.from_mongo(record))
        return price_records

    
    @staticmethod
    async def compare_prices(product_name: str):
        product = await product_collection.find_one({"name": product_name})
        if not product:
            return None
        
        price_records = await PriceRecordService.list_price_records(product_name)
        if not price_records:
            return None
        
        # Simple comparison: find the lowest price
        lowest_price = min(price_records, key=lambda x: x.price)
        highest_price = max(price_records, key=lambda x: x.price)
        
        return {
            "product_name": product_name,
            "lowest_price": {
                "price": lowest_price.price,
                "unit": lowest_price.unit,
                "store": lowest_price.store,
                "date": lowest_price.date
            },
            "highest_price": {
                "price": highest_price.price,
                "unit": highest_price.unit,
                "store": highest_price.store,
                "date": highest_price.date
            },
            "price_difference": highest_price.price - lowest_price.price
        }