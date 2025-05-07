import cv2
import tempfile
import os
import requests
from moviepy import VideoFileClip

def extract_audio_from_video(
    video_bytes: bytes, ext: str, audio_ext: str = ".mp3"
) -> bytes:
    """
    Extract audio from video bytes, return audio bytes (default mp3).
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp_vid:
        tmp_vid.write(video_bytes)
        video_path = tmp_vid.name
    audio_path = video_path + audio_ext
    try:
        video = VideoFileClip(video_path)
        video.audio.write_audiofile(audio_path)
        with open(audio_path, "rb") as f:
            audio_bytes = f.read()
        video.close()
    finally:
        os.unlink(video_path)
        if os.path.exists(audio_path):
            os.unlink(audio_path)
    return audio_bytes

def send_audio_to_transcription_server(
    audio_bytes: bytes, url: str, field_name: str = "file", filename: str = "audio.mp3"
) -> dict:
    """
    Send audio bytes to transcription server, return server response (as dict).
    """
    files = {field_name: (filename, audio_bytes, "audio/mpeg")}
    response = requests.post(url, files=files)
    response.raise_for_status()
    json_response = response.json()
    return json_response

def extract_frames(video_bytes: bytes, ext: str) -> list[bytes]:
    """
    Extract the first frame and every frame at 1-second intervals from the video.
    Returns: list of image bytes (JPEG, base64-encoded).
    """
    # Write video bytes to a temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
        tmp.write(video_bytes)
        video_path = tmp.name

    frames = []
    try:
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            raise RuntimeError("Failed to open video file for frame extraction.")
        fps = cap.get(cv2.CAP_PROP_FPS) or 1
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame_count / fps
        timestamps = [0] + [int(fps * t) for t in range(1, int(duration))]
        seen = set()
        for frame_idx in timestamps:
            if frame_idx >= frame_count or frame_idx in seen:
                continue
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
            ret, frame = cap.read()
            if not ret:
                continue
            import base64
            _, buf = cv2.imencode(".jpg", frame)
            frames.append(base64.b64encode(buf.tobytes()).decode("utf-8"))
            seen.add(frame_idx)
        cap.release()
    finally:
        os.unlink(video_path)

    return frames

def extract_and_ocr_video_frames(video_bytes: bytes, ext: str) -> tuple[str, list[bytes]]:
    """
    Extract frames from video, perform OCR on each, deduplicate text, and return (ocr_text, frames).
    """
    import base64
    from PIL import Image
    import pytesseract
    import io
    frames = extract_frames(video_bytes, ext)
    ocr_texts = []
    seen = set()
    for frame_b64 in frames:
        try:
            frame_bytes = base64.b64decode(frame_b64)
            img = Image.open(io.BytesIO(frame_bytes))
            text = pytesseract.image_to_string(img).strip()
            if text and text not in seen:
                ocr_texts.append(text)
                seen.add(text)
        except Exception:
            continue
    ocr_text = "\n".join(ocr_texts)
    return ocr_text, frames
