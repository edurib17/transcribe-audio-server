from sqlalchemy import Column, String, DateTime
from datetime import datetime
import uuid

from app.core.database import Base

class TranscriptionDetails(Base):
    __tablename__ = "transcription_details"

    uuid = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    transcription = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
