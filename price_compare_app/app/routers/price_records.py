# app/routers/price_records.py
from fastapi import APIRouter, HTTPException
from app.models.price_record import PriceRecordModel
from app.schemas.price_record import PriceRecordCreate, PriceRecordUpdate, PriceRecordInDB
from app.services.price_record_service import PriceRecordService

router = APIRouter()

@router.post("/price_records/", response_model=PriceRecordInDB)
async def create_price_record(price_record: PriceRecordCreate):
    price_record_id = await PriceRecordService.create_price_record(price_record)
    created_record = await PriceRecordService.get_price_record(price_record_id)
    return PriceRecordInDB(**created_record.model_dump())

@router.get("/price_records/{price_record_id}", response_model=PriceRecordInDB)
async def read_price_record(price_record_id: str):
    price_record = await PriceRecordService.get_price_record(price_record_id)
    if price_record is None:
        raise HTTPException(status_code=404, detail="Price record not found")
    return PriceRecordInDB(**price_record.model_dump())

@router.put("/price_records/{price_record_id}", response_model=PriceRecordInDB)
async def update_price_record(price_record_id: str, price_record: PriceRecordUpdate):
    updated = await PriceRecordService.update_price_record(price_record_id, price_record.model_dump(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Price record not found")
    updated_price_record = await PriceRecordService.get_price_record(price_record_id)
    return PriceRecordInDB(**updated_price_record.model_dump())

@router.delete("/price_records/{price_record_id}", response_model=bool)
async def delete_price_record(price_record_id: str):
    deleted = await PriceRecordService.delete_price_record(price_record_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Price record not found")
    return True

@router.get("/price_records/", response_model=list[PriceRecordInDB])
async def list_price_records(product_name: str = None):
    price_records = await PriceRecordService.list_price_records(product_name)
    return [PriceRecordInDB(**record.model_dump()) for record in price_records]

@router.get("/price_records/compare/{product_name}")
async def compare_prices(product_name: str):
    comparison = await PriceRecordService.compare_prices(product_name)
    if comparison is None:
        raise HTTPException(status_code=404, detail="No price records found for this product")
    return comparison
