from fastapi import APIRouter
from app.models.water import WaterData
from app.database import water_collection
from datetime import datetime

router = APIRouter(tags=["Water"])

@router.post("/water")
async def add_water_data(data: WaterData):
    record = data.dict()
    record["date"] = datetime.combine(record["date"], datetime.min.time())
    await water_collection.insert_one(record)
    return {"message": "Water quality data added successfully"}
