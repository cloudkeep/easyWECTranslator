
Python 3.9


**PIP**:

Aby zainstalować wszystkie potrzebne paczki z pip:

pip install -r requirements.txt


Eksport zależności do txt:

pip freeze > requirements.txt



**CONDA**:

Jeżeli chcemy skopiować środowisko to:
- Tworzenie od 0:

conda env create --name easyWECTranslator --file=environment.yml


- Aktualizacja:
conda env update --file environment.yml --prune

- Eksport
conda env export > environment.yml
(uwaga paczki pip na razie się nie synchronizują)


**PAKIETY**:


_openai-whisper_:

pip install openai-whisper

Uwaga dla openai-whisper jest potrzebny ffmpeg,

- na windows instalujemy go za pomocą choco -> instalacja choco https://chocolatey.org/install
później w terminalu -> choco install ffmpeg

- na ubuntu/debian instalujemy tak -> sudo apt update && sudo apt install ffmpeg

- na macos tak -> brew install ffmpeg



_easynmt_:

pip install easynmt

- na windows są potrzebne vsbuildtools, najnowsze https://visualstudio.microsoft.com/visual-cpp-build-tools/
(to dla instalacji fasttext)

- na ubuntu/debian nie potrzebne vsbuildtools



_coquitts_:

pip install TTS

instalacja bez problemów


