from fastapi import FastAPI
from app.routes import (
    hospital_routes,
    water_routes,
    prediction_routes,
    alert_routes
)

app = FastAPI(
    title="OutbreakGuard API",
    description="Predictive Disease Outbreak System",
    version="1.0"
)

app.include_router(hospital_routes.router, prefix="/api")
app.include_router(water_routes.router, prefix="/api")
app.include_router(prediction_routes.router, prefix="/api")
app.include_router(alert_routes.router, prefix="/api")
