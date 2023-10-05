from fastapi import FastAPI, Request, UploadFile, File, HTTPException
from typing import Union
from core.type import Questions
from routes import upload, analyse

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/add/{session_id}")
def upload_file(session_id: str, file: UploadFile = File(...)):
    return upload.upload_file(session_id, file)


@app.post("/analyse/{session_id}")
def analyse_session(session_id: str):
    return analyse.analyse_session(session_id)


@app.post("/uploadQuestions/{session_id}")
def upload_questions(session_id: str, questions: Questions):
    return upload.upload_questions(session_id, questions)
