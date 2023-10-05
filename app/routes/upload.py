# routes/upload.py

from fastapi import FastAPI, UploadFile, File
from pathlib import Path

LOCAL_STORAGE_SOURCE_DIRECTORY = "tmp"


from fastapi import FastAPI, UploadFile, File, HTTPException
from pathlib import Path

LOCAL_STORAGE_SOURCE_DIRECTORY = "tmp"


def upload_file(session_id: str, file: UploadFile = File(...)):
    # Create a directory for the session if doesn't exist
    session_directory = Path(LOCAL_STORAGE_SOURCE_DIRECTORY) / session_id
    session_directory.mkdir(parents=True, exist_ok=True)

    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed!")

    # Save uploaded file to the session directory
    file_path = session_directory / file.filename
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    file.close()

    return {"filename": file.filename, "session_id": session_id}


def upload_questions(session_id: str, questions: str):
    # create a csv file with the questions
    session_directory = Path(LOCAL_STORAGE_SOURCE_DIRECTORY) / session_id
    session_directory.mkdir(parents=True, exist_ok=True)
    file_path = session_directory / "questions.csv"
    with open(file_path, "w") as buffer:
        # iterate over all questions and write them to the file
        for question in questions.questions:
            buffer.write(question + "\n")
    return {"questions": questions, "session_id": session_id}
