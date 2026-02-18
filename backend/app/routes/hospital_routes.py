from fastapi import APIRouter
from datetime import datetime
from app.models.hospital import HospitalData
from app.database import hospital_collection

router = APIRouter(tags=["Hospital"])

@router.post("/hospital")
async def add_hospital_data(data: HospitalData):
    record = data.dict()
    record["date"] = datetime.combine(record["date"], datetime.min.time())
    await hospital_collection.insert_one(record)
    return {"message": "Hospital data added successfully"}
