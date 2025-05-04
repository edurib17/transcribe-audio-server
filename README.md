# 🎙️ transcribe-audio-server

Um servidor de transcrição de áudio construído com FastAPI que utiliza o modelo Whisper da OpenAI para transcrever arquivos de áudio enviados via API. A transcrição é armazenada em um banco de dados SQLite.

---

## 🚀 Tecnologias utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/) (ASGI server)
- [Whisper](https://github.com/openai/whisper)
- [PyTorch](https://pytorch.org/)
- [Torchaudio](https://pytorch.org/audio/)
- [SoundFile](https://pysoundfile.readthedocs.io/)
- [NumPy](https://numpy.org/)
- [python-multipart](https://andrew-d.github.io/python-multipart/)

---

## 📦 Requisitos

Instale os pacotes necessários com:

```bash
pip install -r requirements.txt
