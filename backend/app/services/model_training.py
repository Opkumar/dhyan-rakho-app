import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta
from app.database import hospital_collection, water_collection
from app.services.risk_scoring import calculate_water_risk

model = LinearRegression()
is_trained = False


async def train_model(location: str, disease: str):
    global is_trained

    since = datetime.utcnow() - timedelta(days=14)

    hospital_data = await hospital_collection.find({
        "location": location,
        "disease": disease,
        "date": {"$gte": since}
    }).to_list(100)

    if len(hospital_data) < 5:
        return False  # not enough data

    X = []
    y = []

    hospital_data.sort(key=lambda x: x["date"])

    for i in range(3, len(hospital_data)):
        past_cases = [h["cases"] for h in hospital_data[i-3:i]]
        avg_3 = np.mean(past_cases)
        trend = hospital_data[i]["cases"] - hospital_data[i-3]["cases"]

        water = await water_collection.find_one(
            {"location": location},
            sort=[("date", -1)]
        )

        water_risk = calculate_water_risk(water) if water else 0

        X.append([avg_3, trend, water_risk])
        y.append(hospital_data[i]["cases"])

    model.fit(X, y)
    is_trained = True
    return True
