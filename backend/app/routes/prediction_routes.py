from fastapi import APIRouter, Query
from app.services.forecasting import forecast_cases
from app.services.model_training import train_model
from app.services.risk_scoring import calculate_risk
from app.database import prediction_collection, alert_collection
from datetime import datetime

router = APIRouter(tags=["Prediction"])

@router.get("/predict/{location}")
async def predict_outbreak(
    location: str,
    disease: str = Query(...)
):
    # 1️⃣ Train model (if needed)
    await train_model(location, disease)

    # 2️⃣ Predict outbreak
    predicted_cases, confidence = await forecast_cases(location, disease)
    risk = calculate_risk(predicted_cases)

    # 3️⃣ Prepare prediction document
    prediction = {
        "location": location,
        "disease": disease,
        "predicted_cases_48h": predicted_cases,
        "confidence": confidence,
        "risk_level": risk,
        "generated_at": datetime.utcnow()
    }

    # 4️⃣ Insert into MongoDB
    await prediction_collection.insert_one(prediction)

    # 🚨 DO NOT RETURN ObjectId
    prediction.pop("_id", None)

    # 5️⃣ Generate alert if high risk
    if risk == "High":
        await alert_collection.insert_one({
            "location": location,
            "message": "High outbreak risk detected",
            "risk_level": "High",
            "timestamp": datetime.utcnow(),
            "status": "unread"
        })

    # 6️⃣ Safe JSON response
    return prediction
