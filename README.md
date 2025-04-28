# anyvec

AnyVec is an open-source Python package that makes it easy to vectorize any type of file — text, images, audio, video, or code — through a single, unified interface. Traditionally, embedding different data types (like text vs. images) requires different models and disparate code paths. AnyVec abstracts away these complexities, allowing you to work with a unified API for all your vectorization needs, regardless of file type.

## Building the CLIP Docker Image

To build the Docker image for the CLIP component, run the following commands from the project root:

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
