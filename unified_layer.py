from graph_layer import GraphLayer
from vector_layer import VectorLayer

class UnifiedLayer:
    def __init__(self, graph_weight=0.6, vector_weight=0.4):
        """
        Combines Graph-based and Vector-based scores.
        """
       
        self.graph_layer = GraphLayer()
        self.vector_layer = VectorLayer(model_name="all-MiniLM-L6-v2")
        self.graph_weight = graph_weight
        self.vector_weight = vector_weight

    def compute_unified_score(self, entity_name, query_text, doc_id, doc_text):
        """
        Unified Score = (w_graph × Graph Score) + (w_vector × Vector Score)
        """
        graph_score = self.graph_layer.compute_connectivity_score(entity_name, doc_id)
        vector_score = self.vector_layer.compute_similarity(query_text, doc_text)
        unified = (self.graph_weight * graph_score) + (self.vector_weight * vector_score)
        return round(unified, 4)

    def close(self):
        self.graph_layer.close()
