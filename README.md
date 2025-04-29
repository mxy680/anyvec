# anyvec

AnyVec is an open-source Python package that makes it easy to vectorize any type of file — text, images, audio, video, or code — through a single, unified interface. Traditionally, embedding different data types (like text vs. images) requires different models and disparate code paths. AnyVec abstracts away these complexities, allowing you to work with a unified API for all your vectorization needs, regardless of file type.

---

## Audio Transcription Support (Whisper)

To use audio transcription features (for .mp3, .wav, etc.), you must manually install OpenAI Whisper and ffmpeg:

```bash
pip install git+https://github.com/openai/whisper.git
```

If you're using Poetry, run:

```bash
poetry run pip install git+https://github.com/openai/whisper.git
```

You must also have ffmpeg installed on your system:
- **macOS:** `brew install ffmpeg`
- **Ubuntu/Debian:** `sudo apt-get install ffmpeg`

If Whisper is not installed, attempting to process audio files will result in a clear error message. See the code for details.

---

## Building the CLIP Docker Image

**First, clone this repository and change into the project directory:**

```bash
git clone https://github.com/mxy680/clip-inference.git
cd clip-inference
```

Then, to build the Docker image for the CLIP component, run the following commands from the project root:

```bash
cd clip
LOCAL_REPO="multi2vec-clip" \
  TEXT_MODEL_NAME="sentence-transformers/clip-ViT-B-32-multilingual-v1" \
  CLIP_MODEL_NAME="clip-ViT-B-32" \
  ./scripts/build.sh
```

## Running the CLIP Docker Container

After building the image, run the container and map port 8000 on your host to port 8080 in the container (where the API runs):

```bash
docker run --rm -it -p 8000:8080 multi2vec-clip
```

The API will then be available at http://localhost:8000.

To run the container in detached mode (in the background), use:

```bash
docker run -d -p 8000:8080 multi2vec-clip
```

The API will still be available at http://localhost:8000 while the container runs in the background.
