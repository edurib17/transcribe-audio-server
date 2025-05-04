from fastapi import FastAPI
from app.api import transcribe

from app.core.database import engine, Base 

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Audio Transcription API",
    version="1.0.0"
)

app.include_router(transcribe.router, prefix="/api/v1")