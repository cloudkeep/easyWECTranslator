**PIP**:

Aby zainstalować wszystkie potrzebne paczki z pip:

PyCharm wygodnie patrzy, że nie ma niektórych zależności z requirements.txt(nie zawsze dobrze to działa) i proponuje zainstalować, ale można też ręcznie:

pip install -r requirements.txt

Eksport zależności do txt:

Ręcznie

**CONDA**:

- Tworzymy od 0 na python 3.9:

conda env create --name easyWECTranslator

**PAKIETY**:

_openai-whisper_:

Uwaga dla openai-whisper jest potrzebny ffmpeg,

- na windows instalujemy go za pomocą choco -> instalacja choco https://chocolatey.org/install
później w terminalu -> choco install ffmpeg

- na ubuntu/debian instalujemy tak -> sudo apt update && sudo apt install ffmpeg

- na macos tak -> brew install ffmpeg

_easynmt_:

- na windows są potrzebne vsbuildtools, najnowsze https://visualstudio.microsoft.com/visual-cpp-build-tools/
(to dla instalacji fasttext)

- na ubuntu/debian też potrzebne vsbuildtools

_coquitts_:

instalacja bez problemów


