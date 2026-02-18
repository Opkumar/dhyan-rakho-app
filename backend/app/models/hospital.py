from pydantic import BaseModel
from datetime import date

class HospitalData(BaseModel):
    date: date
    location: str
    disease: str
    cases: int
