import numpy as np

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