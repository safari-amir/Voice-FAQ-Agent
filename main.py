from src import audio_utils
from src import llm_agent
from src import config # Not directly used in run_voice_agent, but good for completeness

def run_voice_agent():
    """
    Orchestrates the full voice agent loop:
    1. Records audio input.
    2. Transcribes audio to text.
    3. Sends text to LLM for a response.
    4. Converts LLM response to speech and plays it.
    """
    print("🎧 Voice Agent is running...")
    
    # 1. Record Live Audio
    audio_path = audio_utils.record_audio()
    if not audio_path:
        print("Audio recording failed. Exiting.")
        return

    # 2. Speech to Text
    print("🧠 Transcribing...")
    text = audio_utils.speech_to_text(audio_path)
    if not text:
        print("Transcription failed. Exiting.")
        return
    print("📝 You said:", text)

    # 3. Send to LLM
    print("🤖 Thinking...")
    response = llm_agent.ask_llm(text)
    if not response:
        print("LLM did not provide a response. Exiting.")
        return
    print("🤖 Bot:", response)

    # 4. Text to Speech and Play
    print("🔊 Speaking...")
    audio_utils.speak_text(response)

    print("✅ Done.")

if __name__ == "__main__":
    run_voice_agent()