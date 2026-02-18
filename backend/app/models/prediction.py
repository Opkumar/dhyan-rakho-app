from pydantic import BaseModel
from datetime import datetime

class Prediction(BaseModel):
    location: str
    disease: str
    predicted_cases_48h: int
    confidence: float
    risk_level: str
    generated_at: datetime
