import numpy as np

# Sample Graph and Vector scores
graph_scores = [0.2, 0.5, 0.8, 1.0]
vector_scores = [0.6, 0.4, 0.9, 0.3]

# Step 1: Convert Graph score range [0,1] → [2,3]
new_graph_scores = [2 + s for s in graph_scores]  # or using formula
print("Converted Graph Scores:", new_graph_scores)

# Step 2: Calculate Unified Score (equal weights)
unified_scores = [(g + v) / 2 for g, v in zip(new_graph_scores, vector_scores)]
print("Unified Scores:", unified_scores)

# Step 3: Normalize Unified Scores between 0 and 1
min_val = min(unified_scores)
max_val = max(unified_scores)
normalized_scores = [(u - min_val) / (max_val - min_val) for u in unified_scores]
print("Normalized Scores:", normalized_scores)

# Step 4: Display neatly
print("\nFinal Results:")
print("Section | Graph | Vector | Unified | Normalized")
for i in range(len(graph_scores)):
    print(f"{i+1:7d} | {new_graph_scores[i]:6.2f} | {vector_scores[i]:6.2f} | {unified_scores[i]:8.2f} | {normalized_scores[i]:10.2f}")
