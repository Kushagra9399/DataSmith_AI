import speech_recognition as sr

from pydub import AudioSegment

import os


def transcribe_audio(file_path):

    recognizer = sr.Recognizer()

    wav_path = file_path

    # ---------- CONVERT MP3 TO WAV ----------
    if file_path.endswith(".mp3"):

        wav_path = file_path.replace(".mp3", ".wav")

        audio = AudioSegment.from_mp3(file_path)

        audio.export(wav_path, format="wav")

    # ---------- TRANSCRIBE ----------
    try:

        with sr.AudioFile(wav_path) as source:

            audio_data = recognizer.record(source)

        text = recognizer.recognize_google(audio_data)

        return text

    except Exception as e:

        print(e)

        return "Audio transcription failed"

    finally:

        # Optional cleanup
        if wav_path != file_path and os.path.exists(wav_path):
            os.remove(wav_path)