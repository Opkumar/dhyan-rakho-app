import asyncio
import random
from datetime import datetime, timedelta
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.ps5_health_db

async def seed():
    hospital_records = []

    start_date = datetime(2026, 1, 1)
    location = "Gurugram"
    disease = "Cholera"

    cases = 2  # starting cases

    # 🔹 100 hospital records (gradual outbreak trend)
    for i in range(100):
        cases += random.choice([0, 1, 1, 2])  # upward trend

        hospital_records.append({
            "date": start_date + timedelta(days=i),
            "location": location,
            "disease": disease,
            "cases": cases
        })

    await db.hospital_admissions.insert_many(hospital_records)

    # 🔹 water quality records (every 5 days)
    water_records = []

    for i in range(0, 100, 5):
        water_records.append({
            "date": start_date + timedelta(days=i),
            "location": location,
            "ph": round(random.uniform(6.0, 7.2), 2),
            "turbidity": round(random.uniform(5.0, 10.0), 2),
            "chlorine": round(random.uniform(0.1, 0.3), 2),
            "bacteria_level": random.choice(["Low", "Medium", "High"])
        })

    await db.water_quality.insert_many(water_records)

    print("✅ 100 hospital records inserted")
    print("✅ Water quality records inserted")

asyncio.run(seed())
