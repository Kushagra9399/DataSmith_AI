import os
import re

from services.pdf_service import extract_pdf_text
from services.ocr_service import extract_image_text
from services.audio_service import transcribe_audio
from services.youtube_service import fetch_youtube_transcript

def is_youtube_url(text):

    youtube_patterns = [
        r"(https?://)?(www\.)?(youtube\.com|youtu\.be)/"
    ]

    for pattern in youtube_patterns:

        if re.search(pattern, text):
            return True

    return False


def extract_content(file_path=None, text=""):

    if text and is_youtube_url(text):

        transcript = fetch_youtube_transcript(text)

        return transcript

    if file_path:
        extension = os.path.splitext(file_path)[1].lower()

        if extension in [".png", ".jpg", ".jpeg"]:
            return extract_image_text(file_path)

        elif extension == ".pdf":
            return extract_pdf_text(file_path)

        elif extension in [".mp3", ".wav", ".m4a"]:
            return transcribe_audio(file_path)

        else:
            return "Unsupported file type"
    
    return text