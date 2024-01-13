from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import asr_whisper
import nmt_easynmt
import tts_coqui

app = FastAPI()

# Dodawanie middleware dla obsługi CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Globalna zmienna do sprawdzania, czy serwer jest zajęty
is_busy = False

@app.post("/translate/")
async def translate(file: UploadFile = File(None), text: str = Form(None), target_language: str = Form(...), source_language: str = Form(...)):
    global is_busy

    # Sprawdzanie, czy serwer jest zajęty
    if is_busy:
        return {"message": "Serwer jest aktualnie zajęty. Proszę spróbować później."}
    is_busy = True

    try:
        # Logika obsługi pliku i tekstu
        if file:
            contents = await file.read()
            with open("temp.wav", "wb") as f:
                f.write(contents)
            text = asr_whisper.transcribe_audio("temp.wav")

        if not text:
            return {"error": "Brak tekstu do przetłumaczenia"}

        # Detekcja języka i tłumaczenie tekstu
        detected_language = nmt_easynmt.detect_language(text)

        if source_language == "auto":
            translated_text = nmt_easynmt.translate_text(detected_language, text, target_language)
        else:
            translated_text = nmt_easynmt.translate_text(source_language, text, target_language)




        # Wybór modelu TTS
        tts_model = {
            "pl": "tts_models/pl/mai_female/vits",
            "en": "tts_models/en/ljspeech/tacotron2-DDC",
            "de": "tts_models/de/thorsten/vits",
            "es": "tts_models/es/css10/vits",
            "it": "tts_models/it/mai_female/vits",
            "fr": "tts_models/fr/css10/vits",
            "uk": "tts_models/uk/mai/vits"

        }
        output_filename = "output.wav"
        tts_coqui.text_to_speech(translated_text, output_filename, tts_model[target_language])

        # Zwracanie wyników
        return {
            "detected_text": text,
            "translated_text": translated_text,
            "detected_language": detected_language,
            "language_pair": detected_language + "-" + target_language,
            "tts_model": tts_model[target_language],
            "file_path": output_filename
        }
    finally:
        # Oznaczenie, że serwer jest ponownie dostępny
        is_busy = False


@app.get("/download/{file_name}")
async def download(file_name: str):
    allowed_files = ["output.wav"]
    if file_name not in allowed_files:
        raise HTTPException(status_code=404, detail="Plik nie został znaleziony")

    return FileResponse(file_name)
