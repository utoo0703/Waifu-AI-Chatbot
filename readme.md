
# Waifu AI Chatbot- Anime Description Generator

This project is an interactive voice-based application that generates random descriptions for anime characters using the Mistral model from HuggingFace. The application takes user input via speech, processes it, and generates detailed descriptions based on predefined options and user-specified features.

## Demo Video
[![Anime Description Generator Demo]([https://img.youtube.com/vi/dQw4w9WgXcQ/0.jpg](https://img.youtube.com/vi/NsUrk8be4s4/hqdefault.jpg))](https://www.youtube.com/watch?v=NsUrk8be4s4)


## Features

- **Voice Interaction:** Utilizes speech recognition to take user input and text-to-speech to provide responses.
- **Random Name Generation:** Generates random names for anime characters using predefined adjective and noun lists.
- **Anime Description Generation:** Uses the Mistral model from HuggingFace to create detailed descriptions of anime characters based on user input.
- **Age Validation:** Ensures users are 18 or older to use the service.
- **Customizable Features:** Allows users to specify custom features for the anime characters.

## Requirements

- Python 3.x
- `speech_recognition` library
- `pyttsx3` library
- `huggingface_hub` library

## Installation

1. Clone the repository:

```sh
git clone https://github.com/your-repo/anime-description-generator.git
cd anime-description-generator
```

2. Install the required packages:

```sh
pip install -r requirements.txt
```

## Usage

1. Run the script:

```sh
python main.py
```

2. Follow the voice prompts to interact with the application.

## Code Overview

### `main.py`

- **Import Libraries:**
  - `random`: For generating random names.
  - `speech_recognition as sr`: For speech recognition.
  - `pyttsx3`: For text-to-speech conversion.
  - `InferenceClient` from `huggingface_hub`: For generating descriptions using the Mistral model.

- **Initialize Recognizer and TTS Engine:**
  - `r = sr.Recognizer()`
  - `engine = pyttsx3.init()`

- **SpeakText Function:**
  Converts text to speech.

- **Inference Client Initialization:**
  Initializes the client for the Mistral model.

- **Generate Description Function:**
  Generates anime descriptions based on user input.

- **Check Age Function:**
  Ensures the user is 18 or older.

- **Get Valid Input Function:**
  Gets user input with validation.

- **Validate Yes/No Function:**
  Validates yes/no user input.

- **Get User Input Function:**
  Gets user input via speech recognition.

- **Generate Random Name Function:**
  Generates random names for anime characters.

- **Validate Anime Choice Function:**
  Validates the user's anime character choice.

- **Main Function:**
  Orchestrates the interaction with the user, processes input, and generates the anime description.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [HuggingFace](https://huggingface.co/) for providing the Mistral model.
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) library for speech recognition.
- [pyttsx3](https://pypi.org/project/pyttsx3/) library for text-to-speech conversion.
