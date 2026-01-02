from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.models import Bottle
from app.models.credit_lineage import CreditLineage
from app.core.exchange import compute_exchange_ratio
from app.db import get_db
import uuid

router = APIRouter(prefix="/credits", tags=["credits"])

@router.post("/roam")
def roam_credit(
    bottle_id: str,
    to_country: str,
    db: Session = Depends(get_db)
):
    credit = db.query(Bottle).filter(Bottle.id == bottle_id).first()
    if not credit:
        raise HTTPException(status_code=404, detail="Credit not found")

    ratio = compute_exchange_ratio(
        credit.country,
        to_country,
        credit.brand
    )

    new_ml = int(credit.remaining_ml * ratio)

    new_credit = Bottle(
        id=str(uuid.uuid4()),
        user_id=credit.user_id,
        brand=credit.brand,
        total_ml=new_ml,
        remaining_ml=new_ml,
        country=to_country,
        state=None
    )

    db.add(new_credit)

    lineage = CreditLineage(
        parent_credit_id=credit.id,
        child_credit_id=new_credit.id,
        from_country=credit.country,
        to_country=to_country,
        exchange_ratio=int(ratio * 100)
    )

    credit.remaining_ml = 0

    db.add(lineage)
    db.commit()

    return {
        "new_credit_id": new_credit.id,
        "remaining_ml": new_ml
    }
