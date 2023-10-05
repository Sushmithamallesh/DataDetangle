# routes/upload.py

from fastapi import FastAPI, UploadFile, File
from pathlib import Path

LOCAL_STORAGE_SOURCE_DIRECTORY = "tmp"


def upload_file(session_id: str, file: UploadFile = File(...)):
    # Create a directory for the session if doesn't exist
    session_directory = Path(LOCAL_STORAGE_SOURCE_DIRECTORY) / session_id
    session_directory.mkdir(parents=True, exist_ok=True)

    # Save uploaded file to the session directory
    file_path = session_directory / file.filename
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    file.close()

    return {"filename": file.filename, "session_id": session_id}
