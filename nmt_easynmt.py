from easynmt import EasyNMT
import sys


def translate_text(text, target_lang, model_name='opus-mt'):
    try:
        model = EasyNMT(model_name)
        return model.translate(text, target_lang=target_lang)
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
        return None


def detect_language(text, model_name='opus-mt'):
    try:
        model = EasyNMT(model_name)
        return model.language_detection(text)
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
        return None


def directions_list(model_name='opus-mt'):
    try:
        model = EasyNMT(model_name)
        return sorted(list(model.lang_pairs))
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
        return None


if __name__ == "__main__":
    text = sys.argv[1]
    target_language = sys.argv[2]
    translated_text = translate_text(text, target_language)
    if translated_text:
        print(translated_text)
    else:
        print("Nie udało się przetłumaczyć tekstu.")
