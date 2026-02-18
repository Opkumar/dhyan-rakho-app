from fastapi import APIRouter
from app.services.forecasting import forecast_cases
from app.services.risk_scoring import calculate_risk
from app.database import prediction_collection, alert_collection
from datetime import datetime

router = APIRouter(tags=["Prediction"])

@router.get("/predict/{location}")
async def predict_outbreak(location: str, disease: str):
    predicted_cases, confidence = forecast_cases(location, disease)
    risk = calculate_risk(predicted_cases)

    prediction = {
        "location": location,
        "disease": disease,
        "predicted_cases_48h": predicted_cases,
        "confidence": confidence,
        "risk_level": risk,
        "generated_at": datetime.utcnow()
    }

    await prediction_collection.insert_one(prediction)

    if risk == "High":
        await alert_collection.insert_one({
            "location": location,
            "message": "High outbreak risk detected",
            "risk_level": "High",
            "timestamp": datetime.utcnow(),
            "status": "unread"
        })

    return prediction
