import io
import tempfile
import base64
from typing import List, Tuple, Optional
from PIL import Image
import cv2

from anyvec.processing.audio import transcribe_audio_whisper


def extract_video_frames_and_audio(
    video_bytes: bytes, frame_interval_sec: int = 1
) -> Tuple[List[str], Optional[str]]:
    """
    Extracts the first frame (thumbnail) and every frame at `frame_interval_sec` intervals,
    returning a list of base64-encoded images and the transcribed audio text.
    """
    with tempfile.NamedTemporaryFile(delete=True, suffix=".mp4") as tmp:
        tmp.write(video_bytes)
        tmp.flush()
        cap = cv2.VideoCapture(tmp.name)
        if not cap.isOpened():
            raise Exception("Could not open video file.")

        fps = cap.get(cv2.CAP_PROP_FPS)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration_sec = total_frames / fps if fps else 0

        frames = []
        timestamps = [0] + [int(fps * t) for t in range(1, int(duration_sec))]
        for ts in timestamps:
            cap.set(cv2.CAP_PROP_POS_FRAMES, ts)
            ret, frame = cap.read()
            if not ret:
                break
            # Convert frame to base64
            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            buffered = io.BytesIO()
            img.save(buffered, format="PNG")
            frames.append(base64.b64encode(buffered.getvalue()).decode("utf-8"))
        cap.release()

        # Extract audio and transcribe
        import subprocess

        text = ""
        try:
            with tempfile.NamedTemporaryFile(delete=True, suffix=".wav") as audio_tmp:
                # Use ffmpeg to extract audio as mono 16kHz PCM WAV
                ffmpeg_cmd = [
                    "ffmpeg",
                    "-y",
                    "-i",
                    tmp.name,
                    "-vn",
                    "-acodec",
                    "pcm_s16le",
                    "-ar",
                    "16000",
                    "-ac",
                    "1",
                    audio_tmp.name,
                ]
                result = subprocess.run(ffmpeg_cmd, capture_output=True)
                if result.returncode != 0:
                    print(f"[ERROR] ffmpeg failed: {result.stderr.decode()}")
                else:
                    with open(audio_tmp.name, "rb") as af:
                        audio_bytes = af.read()
                    if (
                        len(audio_bytes) > 44
                    ):  # WAV header is 44 bytes, so >44 means there's audio
                        text = transcribe_audio_whisper(audio_bytes)
                    else:
                        print("[DEBUG] No audio extracted from video.")
        except Exception as e:
            print(f"[ERROR] Failed to extract or transcribe audio: {e}")
            text = ""

    return frames, text
