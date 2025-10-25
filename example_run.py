from graph_layer import GraphLayer

gl = GraphLayer()
try:
    score = gl.compute_connectivity_score("Lung Cancer", "docA")
    print("Raw Graph Score:", score)
    print("Normalized Graph Score:", gl.normalized_graph_score("Lung Cancer", "docA"))
finally:
    gl.close()
