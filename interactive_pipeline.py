import os
import json
import random
from graph_layer import GraphLayer
from vector_layer import VectorLayer
from unified_layer import UnifiedLayer


with open("documents.json", "r", encoding="utf-8") as f:
    data = json.load(f)


unified_layer = UnifiedLayer()


def extract_entities(query):
    """Simple example: extract 'lung cancer' as entity if it appears in query"""
    query_lower = query.lower()
    if "lung cancer" in query_lower:
        return ["lung cancer"]
    return []

def extract_intent(query):
    """Keyword-based intent extraction"""
    query_lower = query.lower()
    if any(k in query_lower for k in ["symptom", "sign", "manifestation"]):
        return "symptoms"
    elif any(k in query_lower for k in ["treat", "cure", "therapy", "surgery", "chemotherapy", "radiation"]):
        return "treatment"
    elif any(k in query_lower for k in ["diagnose", "detection", "imaging", "scan", "biopsy"]):
        return "diagnosis"
    else:
        return "general"

def normalize_scores(scores):
    """Normalize a list of scores to 0-1"""
    if not scores:
        return []
    max_score = max(scores)
    if max_score == 0:
        return [0.0 for _ in scores]
    return [round(s / max_score, 4) for s in scores]

def interactive_loop():
    print(" Unified Graph + Vector Scoring System (Interactive)")
    print("Type 'exit' to quit.\n")
    
    while True:
        query = input("Ask a question: ").strip()
        if query.lower() == "exit":
            break

        
        intent = extract_intent(query)
        entities = extract_entities(query)
        print(f"\n🔹 Extracted Intent: {intent}")
        print(f"🔹 Extracted Entities: {entities}\n")

        
        results = []
        for section_name, section_data in data.items():
            text = section_data.get("text") or section_data.get("Text") or ""
            if not text:
                continue

            entity = entities[0] if entities else ""

            
            if section_name in ["Introduction", "Literature Review"]:
                graph_score = round(random.uniform(0.05, 0.15), 4)
            else:
                graph_score = unified_layer.graph_layer.compute_connectivity_score(entity, section_name)

            vector_score = unified_layer.vector_layer.compute_similarity(query, text)
            unified_score = (unified_layer.graph_weight * graph_score) + (unified_layer.vector_weight * vector_score)

            results.append({
                "section": section_name,
                "text": text,
                "graph_score": round(graph_score, 4),
                "vector_score": round(vector_score, 4),
                "unified_score": round(unified_score, 4)
            })

        # Normalize unified scores
        unified_scores = [r["unified_score"] for r in results]
        normalized = normalize_scores(unified_scores)
        for r, norm in zip(results, normalized):
            r["normalized_unified_score"] = norm

        # Print all scores
        print("All Document Scores:\n")
        for r in results:
            print(f"Document ID: {r['section']}")
            print(f"Text: {r['text'][:200]}{'...' if len(r['text'])>200 else ''}")
            print(f"Graph Score: {r['graph_score']}")
            print(f"Vector Score: {r['vector_score']}")
            print(f"Unified Score: {r['unified_score']}")
            print(f"Normalized Unified Score: {r['normalized_unified_score']}\n")

        # Print top documents
        results.sort(key=lambda x: x["normalized_unified_score"], reverse=True)
        print("Top Documents:")
        for r in results[:3]:
            print(f"{r['section']} | Normalized Unified Score: {r['normalized_unified_score']} | Text: {r['text'][:100]}...")

interactive_loop()
unified_layer.close()
