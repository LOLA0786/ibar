from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session
from app.models.models import Bottle, Transaction
from app.core.fraud import validate_idempotency
from app.core.compliance import shadow_evaluate
from app.core.security import get_current_user
from app.db import get_db
import uuid, time

router = APIRouter(prefix="/pos", tags=["pos"])

@router.post("/authorize-pour")
def authorize_pour(
    bottle_id: str,
    pour_ml: int,
    scan_id: str = Header(...),
    db: Session = Depends(get_db),
    venue=Depends(get_current_user)
):
    if venue.role != "RESTAURANT":
        raise HTTPException(status_code=403, detail="Not a restaurant")

    validate_idempotency(db, scan_id)

    bottle = db.query(Bottle).filter(Bottle.id == bottle_id).with_for_update().first()
    if not bottle or bottle.remaining_ml < pour_ml:
        raise HTTPException(status_code=400, detail="Insufficient balance")

    decision = shadow_evaluate(
        user_id=bottle.user_id,
        venue_id=venue.id,
        country=venue.country,
        state=venue.state,
        pour_ml=pour_ml
    )

    if decision["block"]:
        raise HTTPException(status_code=403, detail=decision["reason"])

    bottle.remaining_ml -= pour_ml

    txn = Transaction(
        id=str(uuid.uuid4()),
        bottle_id=bottle.id,
        amount_ml=pour_ml,
        venue_id=venue.id,
        scan_id=scan_id,
        timestamp=int(time.time())
    )

    db.add(txn)
    db.commit()

    return {
        "allowed": True,
        "remaining_ml": bottle.remaining_ml
    }
