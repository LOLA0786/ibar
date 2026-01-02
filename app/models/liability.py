from sqlalchemy import Column, String, Boolean
from app.models.models import Base
import uuid, time

class LiabilityEvent(Base):
    __tablename__ = "liability_events"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    venue_id = Column(String)
    transaction_id = Column(String)

    insured = Column(Boolean, default=True)
    resolved = Column(Boolean, default=False)
    created_at = Column(Integer, default=lambda: int(time.time()))
