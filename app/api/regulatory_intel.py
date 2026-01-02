from fastapi import APIRouter
from app.ml.predict import predict_risk

router = APIRouter(prefix="/intel", tags=["intel"])

@router.get("/risk")
def jurisdiction_risk(country: str, state: str):
    risk = predict_risk({
        "country": country,
        "state": state,
        "venue_id": "SIMULATED",
        "pour_ml": 60
    })
    return {"risk_score": risk}
