import PyPDF2
from fastapi import HTTPException
from pathlib import Path

from .upload import LOCAL_STORAGE_SOURCE_DIRECTORY


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from the specified PDF file.

    :param pdf_path: Path to the PDF file.
    :return: Extracted text as a string.
    """
    text = ""

    with open(pdf_path, "rb") as file:
        # Initialize a PDF reader
        pdf_reader = PyPDF2.PdfReader(file)

        # Iterate over all pages in the PDF and extract text
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    return text


def analyse_session(session_id: str):
    # parse the pdf files that are in the session directory
    session_directory = Path(LOCAL_STORAGE_SOURCE_DIRECTORY) / session_id
    if not session_directory.exists():
        raise HTTPException(status_code=404, detail="Session not found!")

    # read all the files in the session directory
    files = session_directory.glob("*.pdf")
    for file in files:
        # parse the file using PyPDF2
        parsed_text = extract_text_from_pdf(file)
        print(f"Extracting File: {file}")
        print(parsed_text)

    return {"success": True}
