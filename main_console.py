import sys
import asr_whisper
import nmt_easynmt
import tts_coqui


def main():
    # Wybór między wprowadzeniem tekstu a przesłaniem pliku audio
    choice = input("Wybierz opcję: [1] Wpisz tekst, [2] Prześlij plik audio: ")

    if choice == '1':
        text = input("Wpisz tekst: ")
    elif choice == '2':
        file_path = input("Podaj ścieżkę do pliku audio: ")
        text = asr_whisper.transcribe_audio(file_path)
    else:
        print("Nieprawidłowa opcja")
        return

    # Wybór języka docelowego
    target_language = input("Wybierz język docelowy (pl, en, de, es): ")

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
    tts_coqui.text_to_speech(translated_text, "output.wav", tts_model[target_language])

    print("Przetłumaczony tekst:", translated_text)
    print("Wygenerowany plik mowy zapisany jako 'output.wav'")


if __name__ == "__main__":
    main()