import numpy as np
import torchaudio
import torch
import soundfile as sf
import os

async def load_audio_from_upload(file):
    contents = await file.read()

    with open("temp_audio", "wb") as f:
        f.write(contents)

    waveform, sample_rate = sf.read("temp_audio", dtype="float32")

    if len(waveform.shape) == 2:
        waveform = np.mean(waveform, axis=1)

    if sample_rate != 16000:
        waveform = torchaudio.functional.resample(
            torch.from_numpy(waveform), sample_rate, 16000
        ).numpy()

       
    os.remove("temp_audio")
    return waveform
