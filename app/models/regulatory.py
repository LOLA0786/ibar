from sqlalchemy import Column, String, Integer, Boolean
from app.models.models import Base
import uuid

class RegulatoryTrace(Base):
    __tablename__ = "regulatory_traces"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    country = Column(String)
    state = Column(String)
    venue_id = Column(String)
    user_id = Column(String)
    pour_ml = Column(Integer)
    decision = Column(String)
    reason = Column(String)
