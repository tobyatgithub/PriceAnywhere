# app/services/product_service.py
from app.models.product import ProductModel
from app.database import database
from bson import ObjectId

product_collection = database.get_collection("products")

class ProductService:
    @staticmethod
    async def create_product(product: ProductModel):
        product_dict = product.to_mongo()
        result = await product_collection.insert_one(product_dict)
        return str(result.inserted_id)

    @staticmethod
    async def get_product(product_id: str):
        product = await product_collection.find_one({"_id": ObjectId(product_id)})
        if product:
            return ProductModel.from_mongo(product)

    @staticmethod
    async def update_product(product_id: str, product_data: dict):
        update_result = await product_collection.update_one(
            {"_id": ObjectId(product_id)}, {"$set": product_data}
        )
        return update_result.modified_count > 0

    @staticmethod
    async def delete_product(product_id: str):
        delete_result = await product_collection.delete_one({"_id": ObjectId(product_id)})
        return delete_result.deleted_count > 0

    @staticmethod
    async def list_products():
        products = []
        async for product in product_collection.find():
            products.append(ProductModel.from_mongo(product))
        return products