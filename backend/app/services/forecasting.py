import numpy as np
from datetime import datetime, timedelta
from app.database import hospital_collection, water_collection
from app.services.risk_scoring import calculate_water_risk
from app.services.model_training import model, is_trained

async def forecast_cases(location: str, disease: str):
    since = datetime.utcnow() - timedelta(days=3)

    hospital_data = await hospital_collection.find({
        "location": location,
        "disease": disease,
        "date": {"$gte": since}
    }).to_list(10)

    if not hospital_data or not is_trained:
        return 5, 0.5  # fallback

    cases = [h["cases"] for h in hospital_data]
    avg_3 = np.mean(cases)
    trend = cases[-1] - cases[0]

    water = await water_collection.find_one(
        {"location": location},
        sort=[("date", -1)]
    )

    water_risk = calculate_water_risk(water) if water else 0

    features = np.array([[avg_3, trend, water_risk]])
    prediction = model.predict(features)[0]

    prediction = max(0, int(round(prediction)))
    confidence = min(0.95, 0.6 + (water_risk * 0.05))

    return prediction, round(confidence, 2)
