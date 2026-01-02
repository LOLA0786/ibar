from sqlalchemy import Column, String, Integer
from app.models.models import Base

class TrustScore(Base):
    __tablename__ = "trust_scores"

    user_id = Column(String, primary_key=True)
    score = Column(Integer, default=50)  # 0–100
