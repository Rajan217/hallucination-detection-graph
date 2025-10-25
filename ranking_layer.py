from unified_layer import UnifiedLayer

class RankingLayer:
    def __init__(self, documents, graph_weight=0.6, vector_weight=0.4):
        """
        Combines Graph and Vector scores into unified ranking results.
        """
        self.documents = documents
        self.unified_layer = UnifiedLayer(graph_weight, vector_weight)

    def compute_scores(self, entity_name, query_text):
        """
        Compute unified scores for each document given a query/entity.
        """
        scores = []
        for doc in self.documents:
            score = self.unified_layer.compute_unified_score(entity_name, query_text, doc['id'], doc['text'])
            scores.append({'id': doc['id'], 'text': doc['text'], 'score': score})
        return scores

    def normalize_scores(self, scores):
        """
        Normalize scores using Min–Max normalization.
        """
        min_score = min(s['score'] for s in scores)
        max_score = max(s['score'] for s in scores)
        for s in scores:
            if max_score - min_score == 0:
                s['norm_score'] = 1.0
            else:
                s['norm_score'] = round((s['score'] - min_score) / (max_score - min_score), 4)
        return scores

    def get_top_n(self, scores, n=3):
        """
        Retrieve top N ranked documents.
        """
        return sorted(scores, key=lambda x: x['norm_score'], reverse=True)[:n]

    def close(self):
        self.unified_layer.close()
