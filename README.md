
# Voice FAQ Assistant
![image](https://github.com/user-attachments/assets/6a16348d-c853-434f-b2e7-92d0bf5afee2)

This project implements a modular voice-enabled assistant designed to answer frequently asked questions (FAQs). It leverages Speech-to-Text (STT) for transcribing user queries, a Large Language Model (LLM) for generating responses based on a provided FAQ context, and Text-to-Speech (TTS) for vocalizing the LLM's answers.


## Features

- **Voice Input:** Records audio from the user's microphone.
- **Speech-to-Text (STT):** Transcribes spoken queries into text using the Whisper model.
- **LLM Integration:** Utilizes an Ollama-hosted LLM (e.g., codellama:7b) to generate concise answers based on a predefined FAQ document.
- **Text-to-Speech (TTS):** Converts the LLM's text responses back into natural-sounding speech using the XTTS-v2 model.
- **Modular Design:** Organized into separate files for configuration, audio utilities, and LLM interaction for better maintainability and scalability.
- **Continuous Interaction:** Allows for multiple back-and-forth voice interactions until the user explicitly exits.

## Project Structure

```

voice_agent_project/
├── main.py # Main entry point, orchestrates the voice agent loop
├── src/
│ ├── config.py # Centralized configuration settings (models, audio, FAQ text)
│ ├── audio_utils.py # Handles audio recording, STT (Whisper), and TTS (XTTS-v2)
│ └── llm_agent.py # Manages LLM interaction (Ollama, Langchain prompts)
└── README.md # This documentation file

```

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8+
- ffmpeg: Required for the Whisper model.
  - Ubuntu/Debian: `sudo apt-get update && sudo apt-get install ffmpeg`
  - macOS: `brew install ffmpeg`
  - Windows: Download from [ffmpeg.org](https://ffmpeg.org) and add it to your system's PATH.
- Ollama: A local LLM server.
  - Download and install Ollama from [ollama.com](https://ollama.com).
  - Pull the codellama:7b model: `ollama pull codellama:7b` (or your preferred model).

## Setup

1. Clone the repository (or create the project structure):
   - If starting from scratch, create a directory named `voice_agent_project` and place the `main.py`, `config.py`, `audio_utils.py`, and `llm_agent.py` files inside it.
2. Navigate into the project directory:
```

cd voice_agent_project

```
3. Install Python dependencies:
- It's highly recommended to use a virtual environment.
```

python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
pip install torch torchaudio transformers sounddevice numpy scipy openai-whisper TTS langchain-ollama langchain-core

```
- Note: The TTS library will download the xtts_v2 model (approx. 10GB) the first time `audio_utils.initialize_audio_models()` is called. This will take some time depending on your internet connection.

## Running the Assistant

- Ensure Ollama is running: Make sure your Ollama server is active and the `codellama:7b` model is available.
- Execute the main script:
```

python main.py

```
- The application will initialize all necessary models (Whisper, TTS, Ollama). This might take a few moments.
- Once initialized, you will see a prompt to speak.
- Speak your question into the microphone.
- Press Enter when you are done speaking.
- The assistant will transcribe your speech, process it with the LLM, and then speak its response.
- The loop will continue, allowing for continuous interaction.
- To exit the application, simply say "exit", "quit", or "خروج" when prompted to speak, and then press Enter.

## Configuration

All configurable parameters are located in `config.py`:
- `DEVICE`: cuda for GPU or cpu for CPU.
- `WHISPER_MODEL`: The Whisper model size (e.g., "base", "small", "medium").
- `TTS_MODEL`: The TTS model path (e.g., "tts_models/multilingual/multi-dataset/xtts_v2").
- `OLLAMA_BASE_URL`: The URL of your local Ollama instance.
- `OLLAMA_MODEL`: The specific Ollama model to use (e.g., "codellama:7b").
- `SAMPLERATE`, `CHANNELS`, `DTYPE`, `BLOCKSIZE`: Audio recording parameters.
- `FAQ_TEXT`: The multiline string containing the frequently asked questions context for the LLM.

## Future Enhancements

- **LangGraph Integration:** Integrate LangGraph for more complex conversational flows, agentic behavior, and tool usage.
- **Error Handling:** More robust error handling and user feedback mechanisms.
- **Customizable Prompts:** Allow for dynamic prompt loading or user-defined prompt templates.
- **GUI:** Develop a simple graphical user interface (GUI) for a more user-friendly experience.
- **Multiple Languages:** Extend support for more languages for both STT and TTS.
- **Streaming Responses:** Implement streaming for faster TTS output during LLM generation.

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

## License

This project is open-source and available under the MIT License.
