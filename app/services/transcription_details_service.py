from sqlalchemy.orm import Session
from app.models.transcription_details import TranscriptionDetails
from app.schemas.transcription_details import TranscriptionDetailsCreate

def create_transcription(db: Session, transcription: TranscriptionDetailsCreate):
   
    db_transcription = TranscriptionDetails(
        transcription=transcription.transcription  
    )
    
    db.add(db_transcription) 
    db.commit()  
    db.refresh(db_transcription) 
    
    return db_transcription



def find_all_transcriptions(db: Session):
    return db.query(TranscriptionDetails).all()