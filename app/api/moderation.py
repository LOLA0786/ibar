from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.abuse import AbuseReport
from app.core.auth import get_current_user

router = APIRouter(prefix="/moderation", tags=["Moderation"])

@router.post("/report")
def report_abuse(
    session_id: str,
    reporter_anon: str,
    reason: str,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    report = AbuseReport(
        session_id=session_id,
        reporter_anon=reporter_anon,
        reason=reason
    )
    db.add(report)
    db.commit()
    return {"status": "reported"}
