from fastapi import APIRouter
from app.models.hospital import HospitalData
from app.database import hospital_collection

router = APIRouter(tags=["Hospital"])

@router.post("/hospital")
async def add_hospital_data(data: HospitalData):
    await hospital_collection.insert_one(data.dict())
    return {"message": "Hospital data added successfully"}
