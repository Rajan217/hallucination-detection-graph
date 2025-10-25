from unified_layer import UnifiedLayer

ul = UnifiedLayer()

entity_name = "Lung Cancer"
doc_text = "Lung cancer symptoms include persistent cough, chest pain, and shortness of breath."
doc_id = "docA"

score = ul.compute_unified_score(entity_name, doc_text, doc_id)
print("Unified Score:", score)

ul.close()
