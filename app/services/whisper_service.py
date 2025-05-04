import whisper
from app.utils.audio import load_audio_from_upload

model = whisper.load_model("small")

async def transcribe_audio(file):
    audio = await load_audio_from_upload(file)
    result = model.transcribe(audio, language="pt", temperature=0)
    return  result["text"]
