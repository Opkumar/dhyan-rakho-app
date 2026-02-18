from pydantic import BaseModel
from datetime import date

class WaterData(BaseModel):
    date: date
    location: str
    ph: float
    turbidity: float
    chlorine: float
    bacteria_level: str
