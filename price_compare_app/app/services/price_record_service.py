# app/services/price_record_service.py
from app.models.price_record import PriceRecordModel
from app.models.product import ProductModel
from app.database import database
from bson import ObjectId
from app.schemas.price_record import PriceRecordCreate, PriceRecordInDB

price_record_collection = database.get_collection("price_records")
product_collection = database.get_collection("products")

class PriceRecordService:
    @staticmethod
    async def create_price_record(price_record: PriceRecordCreate):
        # 查找或创建 product
        product = await product_collection.find_one({"name": price_record.product_name})
        if not product:
            new_product = ProductModel(name=price_record.product_name, category="Unknown")
            result = await product_collection.insert_one(new_product.to_mongo())
            product_id = str(result.inserted_id)
        else:
            product_id = str(product["_id"])

        price_record_dict = price_record.model_dump()
        price_record_dict["product_id"] = product_id
        price_record_model = PriceRecordModel(**price_record_dict)
        mongo_data = price_record_model.to_mongo()
        result = await price_record_collection.insert_one(mongo_data)
        created_record = await PriceRecordService.get_price_record(str(result.inserted_id))
        if created_record:
            return PriceRecordInDB(**created_record.model_dump())
        return None

    @staticmethod
    async def get_price_record(price_record_id: str):
        try:
            price_record = await price_record_collection.find_one({"_id": ObjectId(price_record_id)})
            if price_record:
                product = await product_collection.find_one({"_id": price_record["product_id"]})
                price_record["product_name"] = product["name"] if product else "Unknown"
                return PriceRecordModel.from_mongo(price_record)
        except Exception as e:
            print(f"Error in get_price_record: {e}")
        return None

    @staticmethod
    async def update_price_record(price_record_id: str, price_record_data: dict):
        try:
            update_result = await price_record_collection.update_one(
                {"_id": ObjectId(price_record_id)}, {"$set": price_record_data}
            )
            return update_result.modified_count > 0
        except Exception as e:
            print(f"Error in update_price_record: {e}")
            return False

    @staticmethod
    async def delete_price_record(price_record_id: str):
        try:
            delete_result = await price_record_collection.delete_one({"_id": ObjectId(price_record_id)})
            return delete_result.deleted_count > 0
        except Exception as e:
            print(f"Error in delete_price_record: {e}")
            return False

    @staticmethod
    async def list_price_records(product_name: str = None):
        try:
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
                record["product_name"] = product["name"] if product else "Unknown"
                price_records.append(PriceRecordModel.from_mongo(record))
            return price_records
        except Exception as e:
            print(f"Error in list_price_records: {e}")
            return []

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