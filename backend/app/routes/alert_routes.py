from fastapi import APIRouter
from app.database import alert_collection

router = APIRouter(tags=["Alerts"])

@router.get("/alerts")
async def get_alerts():
    alerts = await alert_collection.find().to_list(100)
    for alert in alerts:
        alert["_id"] = str(alert["_id"])
    return alerts
