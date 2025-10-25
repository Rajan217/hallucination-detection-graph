from ranking_layer import RankingLayer

# Example documents
documents = [
    {'id': 'docA', 'text': "Lung cancer symptoms include persistent cough, chest pain, and shortness of breath."},
    {'id': 'docB', 'text': "Diagnosis methods include imaging, biopsy, and blood tests."},
    {'id': 'docC', 'text': "Treatment options are surgery, chemotherapy, and radiation therapy."}
]

entity_name = "Lung Cancer"

rl = RankingLayer(documents)
scores = rl.compute_scores(entity_name)
scores = rl.normalize_scores(scores)
top_docs = rl.get_top_n(scores, n=2)

print("All Normalized Scores:")
for s in scores:
    print(s)

print("\nTop Documents:")
for s in top_docs:
    print(s)

rl.close()
