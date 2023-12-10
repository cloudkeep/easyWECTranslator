import torch
from TTS.api import TTS
import sys

def text_to_speech(text, output_path, model_name):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    tts = TTS(model_name=model_name, progress_bar=False).to(device)
    tts.tts_to_file(text=text, file_path=output_path)

if __name__ == "__main__":
    text = sys.argv[1]
    output_path = sys.argv[2]
    model_name = sys.argv[3]
    text_to_speech(text, output_path, model_name)