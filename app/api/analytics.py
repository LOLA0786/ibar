from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.models import Transaction
from app.core.security import get_current_user
from app.db import get_db

router = APIRouter(prefix="/analytics", tags=["analytics"])

@router.get("/yearly")
def yearly_summary(db: Session = Depends(get_db), user=Depends(get_current_user)):
    txns = db.query(Transaction).filter(Transaction.user_id == user.id).all()

    total_ml = sum(t.amount_ml for t in txns)
    total_pours = len(txns)

    return {
        "year": 2026,
        "total_ml": total_ml,
        "total_pours": total_pours
    }
