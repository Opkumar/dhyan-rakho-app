from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import (
    hospital_routes,
    water_routes,
    prediction_routes,
    alert_routes
)

app = FastAPI(
    title="Dhyan Rakho App API",
    version="1.0"
)

# ✅ CORS CONFIGURATION
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",   # React dev server
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(hospital_routes.router, prefix="/api")
app.include_router(water_routes.router, prefix="/api")
app.include_router(prediction_routes.router, prefix="/api")
app.include_router(alert_routes.router, prefix="/api")

