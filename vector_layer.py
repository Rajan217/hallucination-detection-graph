# vector_layer.py

from sentence_transformers import SentenceTransformer, util
import torch

class VectorLayer:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        """Initialize local SentenceTransformer model."""
        self.model = SentenceTransformer(model_name)

    def embed_text(self, text: str):
        """Generate embeddings for a given text string."""
        return self.model.encode(text, convert_to_tensor=True)

    def compute_similarity(self, query: str, document: str):
        """
        Compute cosine similarity between query and document embeddings.
        Returns a float between -1 and 1.
        """
        query_emb = self.embed_text(query)
        doc_emb = self.embed_text(document)
        cosine_sim = util.cos_sim(query_emb, doc_emb).item()
        return round(float(cosine_sim), 4)

    def normalized_vector_score(self, query: str, document: str):
        """
        Convert cosine similarity (range -1 to 1) into normalized [0, 1] score.
        """
        sim = self.compute_similarity(query, document)
        norm = (sim + 1.0) / 2.0
        return round(norm, 4)
