import os
import socket

from fastapi import FastAPI

app = FastAPI(title="airgap-api")

VERSION = os.getenv("APP_VERSION", "dev")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/info")
def info():
    return {"version": VERSION, "hostname": socket.gethostname()}
