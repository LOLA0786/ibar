from sqlalchemy import Column, String, DateTime, Boolean
from app.models.models import Base
from datetime import datetime, timedelta
import uuid

def gen_id():
    return str(uuid.uuid4())

class RoamingRoom(Base):
    __tablename__ = "roaming_rooms"

    id = Column(String, primary_key=True, default=gen_id)
    cluster_id = Column(String, index=True)  # e.g. DXB_AIRPORT
    window_start = Column(DateTime, default=datetime.utcnow)
    window_end = Column(DateTime)
    active = Column(Boolean, default=True)

    def __init__(self, cluster_id):
        self.cluster_id = cluster_id
        self.window_start = datetime.utcnow()
        self.window_end = self.window_start + timedelta(minutes=45)
