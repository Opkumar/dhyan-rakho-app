from pydantic import BaseModel
from datetime import datetime

class Alert(BaseModel):
    location: str
    message: str
    risk_level: str
    timestamp: datetime
    status: str = "unread"
