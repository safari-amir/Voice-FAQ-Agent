import tempfile
import os
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write, read
import whisper
from TTS.api import TTS
import torch

# Import configuration settings
import src.config as config

# Initialize TTS model globally to avoid re-loading on each call
try:
    tts = TTS(config.TTS_MODEL).to(config.DEVICE)
except Exception as e:
    print(f"Error initializing TTS model: {e}")
    print("Please ensure the TTS model is downloaded and accessible.")
    tts = None # Set to None if initialization fails

def record_audio():
    """
    Records audio from the microphone until the user presses Enter.
    Returns the path to the temporary WAV file.
    """
    print("🎙️ Speak now. Press Enter to stop recording.")
    recorded = []

    def callback(indata, frames, time, status):
        """Callback function for sounddevice.InputStream."""
        if status:
            print("⚠️", status)
        recorded.append(indata.copy())

    with sd.InputStream(
        samplerate=config.SAMPLERATE,
        channels=config.CHANNELS,
        dtype=config.DTYPE,
        callback=callback
    ):
        input("🔴 Press Enter to stop...\n")

    audio = np.concatenate(recorded, axis=0)
    # Create a temporary file to save the recorded audio
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        write(f.name, config.SAMPLERATE, audio)
        return f.name

def speech_to_text(audio_path):
    """
    Transcribes audio from a given WAV file path to text using Whisper.
    Cleans up the temporary audio file after transcription.
    """
    try:
        model = whisper.load_model(config.WHISPER_MODEL)
        result = model.transcribe(audio_path, language="en")
        return result["text"]
    except Exception as e:
        print(f"Error during speech-to-text transcription: {e}")
        return ""
    finally:
        if os.path.exists(audio_path):
            os.remove(audio_path)  # Clean up temp file

def speak_text(text, speaker="Claribel Dervla", language="en"):
    """
    Converts text to speech using the TTS model and plays the audio.
    Cleans up the temporary audio file after playback.
    """
    if tts is None:
        print("TTS model not initialized. Cannot speak text.")
        return

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        try:
            tts.tts_to_file(text=text, speaker=speaker, language=language, file_path=f.name)
            # Read and play the audio
            rate, data = read(f.name)
            sd.play(data, rate)
            sd.wait()
        except Exception as e:
            print(f"Error during text-to-speech or playback: {e}")
        finally:
            if os.path.exists(f.name):
                os.remove(f.name)