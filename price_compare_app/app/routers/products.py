# app/routers/products.py
from fastapi import APIRouter, HTTPException
from app.models.product import ProductModel
from app.schemas.product import ProductCreate, ProductUpdate, ProductInDB
from app.services.product_service import ProductService

router = APIRouter()

@router.post("/products/", response_model=ProductInDB)
async def create_product(product: ProductCreate):
    product_model = ProductModel(**product.model_dump())
    product_id = await ProductService.create_product(product_model)
    return ProductInDB(_id=str(product_id), **product.model_dump())

@router.get("/products/{product_id}", response_model=ProductInDB)
async def read_product(product_id: str):
    product = await ProductService.get_product(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return ProductInDB(**product.model_dump())

@router.put("/products/{product_id}", response_model=ProductInDB)
async def update_product(product_id: str, product: ProductUpdate):
    updated = await ProductService.update_product(product_id, product.model_dump(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    updated_product = await ProductService.get_product(product_id)
    return ProductInDB(**updated_product.model_dump())

@router.delete("/products/{product_id}", response_model=bool)
async def delete_product(product_id: str):
    deleted = await ProductService.delete_product(product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return True

@router.get("/products/", response_model=list[ProductInDB])
async def list_products():
    products = await ProductService.list_products()
    return [ProductInDB(**product.model_dump()) for product in products]