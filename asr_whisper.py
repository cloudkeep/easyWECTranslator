import whisper
import sys


def transcribe_audio(file_path):
    # Załaduj model WhisperAI
    model = whisper.load_model("base")

    # Przetwórz plik audio
    result = model.transcribe(file_path)

    # Zwróć przetłumaczony tekst
    return result["text"]


if __name__ == "__main__":
    # Pobierz ścieżkę pliku z argumentów linii komend
    audio_file_path = sys.argv[1] if len(sys.argv) > 1 else "./VK-Slyszec-PL-16kHz-16bit.wav"

    # Wykonaj transkrypcję
    transcribed_text = transcribe_audio(audio_file_path)
    print(transcribed_text)
