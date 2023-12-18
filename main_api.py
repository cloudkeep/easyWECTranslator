from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import asr_whisper
import nmt_easynmt
import tts_coqui
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Dla celów rozwojowych, dozwolone są wszystkie źródła
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/translate/")
async def translate(file: UploadFile = File(None), text: str = Form(None), target_language: str = Form(...)):
    # Sprawdzanie, czy przesłano plik czy tekst
    if file:
        contents = await file.read()
        with open("temp.wav", "wb") as f:
            f.write(contents)
        text = asr_whisper.transcribe_audio("temp.wav")

    if not text:
        return {"error": "Brak tekstu do przetłumaczenia"}

    #Detekcja języka
    detected_language = nmt_easynmt.detect_language(text)
    # Tłumaczenie tekstu
    translated_text = nmt_easynmt.translate_text(text, target_language)

    # Wybór modelu TTS
    tts_model = {
        "pl": "tts_models/pl/mai_female/vits",
        "en": "tts_models/en/ljspeech/tacotron2-DDC",
        "de": "tts_models/de/thorsten/vits",
        "es": "tts_models/es/css10/vits",
    }
    output_filename = "output.wav"
    tts_coqui.text_to_speech(translated_text, output_filename, tts_model[target_language])

    # Zapisywanie przetłumaczonego tekstu do tymczasowego pliku
    translated_file_path = "translated_text.txt"
    with open(translated_file_path, "w") as text_file:
        text_file.write(translated_text)

    # Zwracanie ścieżki do pliku z przetłumaczonym tekstem
    return {"translated_text": translated_text, "file_path": output_filename}


@app.get("/download/{file_path}")
async def download(file_path: str):
    return FileResponse(file_path)