from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class TranscriptionDetailsCreate(BaseModel):
    transcription: str

class TranscriptionDetailsResponse(BaseModel):
    uuid: UUID
    transcription: str
    created_at: datetime

    class Config:
        orm_mode = True
        from_attributes = True