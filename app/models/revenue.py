from sqlalchemy import Column, String, Integer
from app.models.models import Base
import uuid, time

class RevenueEvent(Base):
    __tablename__ = "revenue_events"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    source = Column(String)          # POS, INSURANCE, ANALYTICS
    venue_id = Column(String)
    amount = Column(Integer)         # smallest currency unit
    currency = Column(String)
    created_at = Column(Integer, default=lambda: int(time.time()))
