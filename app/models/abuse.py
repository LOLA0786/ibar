from sqlalchemy import Column, String, DateTime
from app.models.models import Base
from datetime import datetime
import uuid

class AbuseReport(Base):
    __tablename__ = "abuse_reports"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    session_id = Column(String)
    reporter_anon = Column(String)
    reason = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
