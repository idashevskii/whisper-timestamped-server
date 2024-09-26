import logging
import os
from typing import List
from fastapi import FastAPI, HTTPException
import whisper_timestamped as whisper
import torch
from pydantic import BaseModel
import base64
import tempfile

logging.basicConfig(level=os.environ.get("LOG_LEVEL", "WARNING").upper())

logger = logging.getLogger(__name__)


app = FastAPI()


class Word(BaseModel):
    text: str
    start: float
    end: float


class TranscribeInput(BaseModel):
    language: str
    audio: str


@app.post("/transcribe")
def do_transcribe(body: TranscribeInput) -> List[Word]:
    with tempfile.NamedTemporaryFile() as tmp:
        try:
            decoded_audio = base64.b64decode(body.audio)
        except:
            raise HTTPException(400, "Failed to decode base64")
        tmp.write(decoded_audio)
        try:
            audio = whisper.load_audio(tmp.name)
        except:
            raise HTTPException(400, "Failed to decode audio")

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = whisper.load_model("tiny", device=device)
    result = whisper.transcribe(model, audio, vad=True, language=body.language)

    ret: List[Word] = []

    for segment in result["segments"]:
        for word in segment["words"]:
            ret.append(Word(text=word["text"], start=word["start"], end=word["end"]))

    return ret


@app.get("/")
def read_root():
    return {"version": "1.0.0"}
