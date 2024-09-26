import logging
import os
from fastapi import FastAPI

logging.basicConfig(level=os.environ.get("LOG_LEVEL", "WARNING").upper())

logger = logging.getLogger(__name__)


app = FastAPI()

@app.get("/")
def read_root():
    return {"version": "1.0.0"}
