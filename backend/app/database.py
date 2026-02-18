from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017"

client = AsyncIOMotorClient(MONGO_URI)
db = client.ps5_health_db

hospital_collection = db.hospital_admissions
water_collection = db.water_quality
prediction_collection = db.predictions
alert_collection = db.alerts
