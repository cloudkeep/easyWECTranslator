import whisper
import sys


def transcribe_audio(file_path):
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return result["text"]


def whisper_detect(file_path):
    model = whisper.load_model("base")
    audio = whisper.load_audio(file_path)
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    _, probs = model.detect_language(mel)
    detected_language = max(probs, key=probs.get)
    print(f"Detected language: {detected_language}")
    return detected_language


if __name__ == "__main__":
    audio_file_path = sys.argv[1]
    transcribed_text = transcribe_audio(audio_file_path)
    print(transcribed_text)
