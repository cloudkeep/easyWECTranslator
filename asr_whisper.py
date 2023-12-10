import whisper
import sys


def transcribe_audio(file_path):
    model = whisper.load_model("tiny")
    result = model.transcribe(file_path)
    return result["text"]


if __name__ == "__main__":
    audio_file_path = sys.argv[1]
    transcribed_text = transcribe_audio(audio_file_path)
    print(transcribed_text)
