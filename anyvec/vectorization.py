import numpy as np
import requests
from anyvec.exceptions import APIConnectionError


def cosine_similarity(v1, v2):
    """
    Computes the cosine similarity between two vectors.

    Args:
        v1 (np.array): First vector.
        v2 (np.array): Second vector.
    Returns:
        float: Cosine similarity.
    """
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    return dot_product / (norm_v1 * norm_v2)


class Vectorizer:
    def __init__(self, client):
        self.client = client

    def vectorize(self, text: str, images: list[bytes]):
        """
        Vectorizes a file and returns the vector

        Args:
            text (str): Text content.
            images list[bytes]: Image content.
            file_name (str): Full file name (e.g., "document.pdf").
            **kwargs: Additional parameters.
        Returns:
            dict: Success status and collection name.
        """
        req_body = {
            "texts": [text],
            "images": images,
        }
        
        try:
            res = requests.post(self.client.url + "/vectorize", json=req_body)
            resBody = res.json()
            text_vectors = resBody["textVectors"]
            image_vectors = resBody["imageVectors"]

            vectors = np.array(text_vectors + image_vectors)
            aggregated_vector = np.mean(vectors, axis=0)
            return aggregated_vector.tolist()

        except requests.RequestException as e:
            raise APIConnectionError(self.client.url, f"Request failed: {e}")
