from sqlalchemy import Column, String, Boolean
from app.models.models import Base
import uuid

class Venue(Base):
    __tablename__ = "venues"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String)
    social_enabled = Column(Boolean, default=True)
