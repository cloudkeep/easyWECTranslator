import torch
from TTS.api import TTS

# Ustaw urządzenie na GPU jeśli jest dostępne, w przeciwnym razie użyj CPU
device = "cuda" if torch.cuda.is_available() else "cpu"

# Inicjalizacja Coqui TTS z wybranym modelem
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False).to(device)

# Tekst do przekształcenia na mowę
text = "Listening does not mean hearing, for hearing is a sense, while listening is an art."

# Ścieżka do zapisania wygenerowanego pliku dźwiękowego
output_path = "output.wav"

# Generowanie mowy i zapis do pliku
tts.tts_to_file(text=text, file_path=output_path)