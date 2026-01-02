from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
import uuid

from app.db import get_db
from app.core.auth import get_current_user
from app.models.roaming_social import RoamingRoom
from app.models.venue_social import RoomMember

router = APIRouter(prefix="/roaming", tags=["Roaming Social"])

def anon_id():
    return "guest-" + uuid.uuid4().hex[:6]

@router.post("/join")
def join_roaming_room(
    cluster_id: str,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    now = datetime.utcnow()

    room = db.query(RoamingRoom).filter(
        RoamingRoom.cluster_id == cluster_id,
        RoamingRoom.window_end > now,
        RoamingRoom.active == True
    ).first()

    if not room:
        room = RoamingRoom(cluster_id)
        db.add(room)
        db.commit()
        db.refresh(room)

    member = RoomMember(
        room_id=room.id,
        anon_id=anon_id()
    )
    db.add(member)
    db.commit()

    return {
        "room_id": room.id,
        "anon_id": member.anon_id,
        "expires_at": room.window_end
    }
