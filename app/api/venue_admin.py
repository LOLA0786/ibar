from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.venue import Venue
from app.core.auth import get_current_user

router = APIRouter(prefix="/venue/admin", tags=["Venue Admin"])

@router.post("/toggle-social")
def toggle_social(
    venue_id: str,
    enabled: bool,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    venue = db.query(Venue).filter(Venue.id == venue_id).first()
    venue.social_enabled = enabled
    db.commit()
    return {"venue_id": venue_id, "social_enabled": enabled}
