from fastapi import APIRouter, HTTPException
import time, hmac, hashlib

router = APIRouter(prefix="/hardware", tags=["hardware"])

SECRET = b"ibar-hardware-secret"

def sign(payload: str):
    return hmac.new(SECRET, payload.encode(), hashlib.sha256).hexdigest()

@router.post("/unlock-spout")
def unlock_spout(bottle_id: str, pour_ml: int, signature: str):
    payload = f"{bottle_id}:{pour_ml}"

    if sign(payload) != signature:
        raise HTTPException(status_code=403, detail="Invalid hardware signature")

    unlock_ms = int((pour_ml / 60) * 4000)  # calibrated pour time

    return {
        "unlock_ms": unlock_ms,
        "expires_at": int(time.time()) + 5
    }
