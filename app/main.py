from fastapi import FastAPI, UploadFile, File, HTTPException
from typing import Union
from routes import upload

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/add/{session_id}")
def upload_file(session_id: str, file: UploadFile = File(...)):
    return upload.upload_file(session_id, file)
