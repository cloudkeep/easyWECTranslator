from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
import asr_whisper
import nmt_easynmt
import tts_coqui
import os

app = FastAPI()

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

    # Tłumaczenie tekstu
    translated_text = nmt_easynmt.translate_text(text, target_language)

    # Wybór modelu TTS
    tts_model = {
        "pl": "tts_models/pl/mai_female/vits",
        "en": "tts_models/en/ljspeech/tacotron2-DDC",
        "de": "tts_models/de/thorsten/vits",
        "es": "tts_models/es/css10/vits",
    }

    # Generowanie mowy
    output_filename = "output.wav"
    tts_coqui.text_to_speech(translated_text, output_filename, tts_model[target_language])

    # Zwracanie pliku i przetłumaczonego tekstu
    return {
        "translated_text": translated_text,
        "file": FileResponse(output_filename)
    }
