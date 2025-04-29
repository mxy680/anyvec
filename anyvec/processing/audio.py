import tempfile
from typing import Optional


def transcribe_audio_whisper(
    audio_bytes: bytes, model: str = "base", language: Optional[str] = None
) -> str:
    """
    Transcribe audio using OpenAI Whisper (via openai-whisper CLI or whisper package).
    Requires the 'whisper' Python package (https://github.com/openai/whisper).
    """
    try:
        import whisper
    except ImportError:
        raise ImportError(
            "The 'openai-whisper' package is required for audio transcription. "
            "Install it with: pip install git+https://github.com/openai/whisper.git"
        )
    with tempfile.NamedTemporaryFile(delete=True, suffix=".wav") as tmp:
        tmp.write(audio_bytes)
        tmp.flush()
        model_obj = whisper.load_model(model)
        result = model_obj.transcribe(tmp.name, language=language)
        return result["text"].strip()
