from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import uuid

from app.db import get_db
from app.core.auth import get_current_user
from app.models.venue_social import VenueRoom, RoomMember, PairSession

router = APIRouter(prefix="/venue", tags=["Venue Social"])

def anon_id():
    return "guest-" + uuid.uuid4().hex[:6]


@router.post("/join")
def join_venue_room(
    venue_id: str,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    now = datetime.utcnow()

    room = db.query(VenueRoom).filter(
        VenueRoom.venue_id == venue_id,
        VenueRoom.window_end > now
    ).first()

    if not room:
        room = VenueRoom(venue_id)
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


@router.get("/room/{room_id}")
def room_presence(
    room_id: str,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    members = db.query(RoomMember).filter(
        RoomMember.room_id == room_id,
        RoomMember.active == True
    ).all()

    return {
        "count": len(members),
        "participants": [{"anon_id": m.anon_id} for m in members]
    }


@router.post("/connect")
def request_pair(
    room_id: str,
    target_anon: str,
    my_anon: str,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    session = PairSession(
        room_id=room_id,
        anon_a=my_anon,
        anon_b=target_anon,
        expires_at=datetime.utcnow() + timedelta(minutes=30)
    )
    db.add(session)
    db.commit()

    return {
        "session_id": session.id,
        "expires_at": session.expires_at
    }
