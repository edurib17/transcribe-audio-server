from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
from app.services.whisper_service import transcribe_audio
from app.services.transcription_details_service import create_transcription, find_all_transcriptions
from app.core.database import get_db 
from app.schemas.transcription_details import TranscriptionDetailsCreate, TranscriptionDetailsResponse

router = APIRouter()

@router.post("/transcribes")
async def transcribe(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if file.content_type not in ["audio/ogg", "audio/mp3"]:
        raise HTTPException(status_code=400, detail="Invalid file type.")

    result_text = await transcribe_audio(file)

    transcription_data = TranscriptionDetailsCreate(transcription=result_text)

    transcription_saved = create_transcription(db, transcription_data)

    return {
        "uuid": transcription_saved.uuid,
        "transcription": transcription_saved.transcription,
        "created_at": transcription_saved.created_at
    }



@router.get("/transcribes")
async def transcribes(db: Session = Depends(get_db)):
    transcribes = find_all_transcriptions(db)
    return [TranscriptionDetailsResponse.from_orm(t) for t in transcribes]


