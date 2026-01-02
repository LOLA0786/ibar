from fastapi import HTTPException
from app.models.models import Transaction

def validate_idempotency(db, scan_id: str):
    exists = db.query(Transaction).filter(Transaction.scan_id == scan_id).first()
    if exists:
        raise HTTPException(status_code=409, detail="Duplicate scan detected")
