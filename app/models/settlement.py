from sqlalchemy import Column, String, Integer, Boolean
from app.models.models import Base
import uuid, time

class VenueSettlement(Base):
    __tablename__ = "venue_settlements"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    bottle_id = Column(String)
    venue_id = Column(String)

    poured_ml = Column(Integer)
    price_per_ml = Column(Integer)   # smallest currency unit
    currency = Column(String)

    settled = Column(Boolean, default=False)
    created_at = Column(Integer, default=lambda: int(time.time()))
