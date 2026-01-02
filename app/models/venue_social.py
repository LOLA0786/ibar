from sqlalchemy import Column, String, DateTime, ForeignKey, Boolean
from app.models.models import Base
from datetime import datetime, timedelta
import uuid

def gen_id():
    return str(uuid.uuid4())

class VenueRoom(Base):
    __tablename__ = "venue_rooms"

    id = Column(String, primary_key=True, default=gen_id)
    venue_id = Column(String, index=True)
    window_start = Column(DateTime, default=datetime.utcnow)
    window_end = Column(DateTime)

    def __init__(self, venue_id):
        self.venue_id = venue_id
        self.window_start = datetime.utcnow()
        self.window_end = self.window_start + timedelta(minutes=30)


class RoomMember(Base):
    __tablename__ = "venue_room_members"

    id = Column(String, primary_key=True, default=gen_id)
    room_id = Column(String, ForeignKey("venue_rooms.id"))
    anon_id = Column(String, index=True)
    joined_at = Column(DateTime, default=datetime.utcnow)
    active = Column(Boolean, default=True)


class PairSession(Base):
    __tablename__ = "venue_pair_sessions"

    id = Column(String, primary_key=True, default=gen_id)
    room_id = Column(String, ForeignKey("venue_rooms.id"))
    anon_a = Column(String)
    anon_b = Column(String)
    expires_at = Column(DateTime)
    active = Column(Boolean, default=True)
