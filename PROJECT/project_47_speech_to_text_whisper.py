PROJECT = {
    "name": "Speech-to-Text (Whisper Tiny)",
    "icon": "🎤",
    "dataset": "OpenAI Whisper",
    "description": "Convert speech to text using Whisper ASR.",
    "steps": "Load Whisper → Transcribe → Output text",
    "code": """
import whisper

model = whisper.load_model("tiny")
result = model.transcribe("audio.mp3")

print(result["text"])
"""
}
