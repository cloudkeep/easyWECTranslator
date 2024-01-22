from PyQt5.QtWidgets import QApplication, QFileDialog
import sys

import asr_whisper
import nmt_easynmt
import tts_coqui
import time


def select_audio_file():
    app = QApplication(sys.argv)
    file_path, _ = QFileDialog.getOpenFileName()
    return file_path


def main():
    # Wybór między wprowadzeniem tekstu a przesłaniem pliku audio
    choice = input("Wybierz opcję: [1] Wpisz tekst, [2] Prześlij plik audio: ")
    file_path = ""
    if choice == '1':
        text = input("Wpisz tekst: ")

    elif choice == '2':
        print("Wybierz plik audio...")
        file_path = select_audio_file()
        if file_path:
            text = asr_whisper.transcribe_audio(file_path)
            detected_language_whisper = asr_whisper.whisper_detect(file_path)
        else:
            print("Nie wybrano pliku.")
            return
    else:
        print("Nieprawidłowa opcja")
        return

    # Wybór języka docelowego
    source_language = input("Wybierz język źródłowy (pl, en, de, es, it, uk, fr): ")
    target_language = input("Wybierz język docelowy (pl, en, de, es, it, uk, fr): ")

    # Wykryty język
    detected_language = nmt_easynmt.detect_language(text)
    detected_language = source_language
    print("Wykryty język:", detected_language)
    # Kierunek tłumaczenia
    language_direction = detected_language + "-" + target_language
    print("Kierunek tłumaczenia:", language_direction)

    directions_list = nmt_easynmt.directions_list()

    if language_direction in directions_list:
        print("OK")
        available_pairs = [pair for pair in directions_list if pair.startswith(detected_language)]
        print("Więcej dostępnych kierunków tłumaczenia:", available_pairs)
    else:
        print("Oczekiwane tłumaczenie nie jest dostępne")
        available_pairs = [pair for pair in directions_list if pair.startswith(detected_language)]
        print("Dostępne kierunki tłumaczenia:", available_pairs)

    # Tłumaczenie tekstu
    start_time = time.time()
    translated_text = nmt_easynmt.translate_text(detected_language, text, target_language)
    print("Przetłumaczony tekst:", translated_text)
    print("Przetłumaczone w czasie {:.2f} s".format(time.time() - start_time))

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
    clone = input("Wybierz opcję: [1] klonuj, [2] nie klonuj: ")

    if clone == '1':
        tts_coqui.text_to_speech(translated_text, "output1.wav", tts_model[target_language], file_path, use_vc=True)

    elif clone == '2':
        tts_coqui.text_to_speech(translated_text, "output1.wav", tts_model[target_language],file_path)

        # Generowanie mowy
    print("Wygenerowany plik mowy zapisany jako 'output.wav'")


if __name__ == "__main__":
    main()
