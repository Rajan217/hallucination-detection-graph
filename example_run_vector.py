# example_run_vector.py

from vector_layer import VectorLayer

vl = VectorLayer()

query = "What are the symptoms of lung cancer?"
doc = "Lung cancer symptoms include persistent cough, chest pain, and shortness of breath."

raw_score = vl.compute_similarity(query, doc)
norm_score = vl.normalized_vector_score(query, doc)

print("Raw Vector Similarity:", raw_score)
print("Normalized Vector Score:", norm_score)
