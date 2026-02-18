from fastapi import APIRouter
from app.models.water import WaterData
from app.database import water_collection

router = APIRouter(tags=["Water"])

@router.post("/water")
async def add_water_data(data: WaterData):
    await water_collection.insert_one(data.dict())
    return {"message": "Water quality data added successfully"}
