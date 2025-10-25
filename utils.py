# utils.py
import spacy
import json

nlp = spacy.load("en_core_web_sm")

def load_documents_from_json(json_file):
    """
    Load JSON where top-level keys are section names (Abstract, Methodology, etc.).
    Returns list of dicts with 'id' and 'text'.
    """
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    documents = []
    for section, content in data.items():
        # Some sections use "text", some "Text"
        text = content.get("text") or content.get("Text") or ""
        if text:
            documents.append({"id": section, "text": text})
    return documents


def extract_intent_entities(question):
    """
    Extract intent and entities.
    Multi-word entities like 'lung cancer' are detected correctly.
    """
    doc = nlp(question)
    # Extract named entities
    entities = [ent.text.lower() for ent in doc.ents]

    # Fallback to noun chunks if no entities
    if not entities:
        entities = [" ".join(chunk.text.lower().split()) for chunk in doc.noun_chunks]

    
    if entities:
        entities = [max(entities, key=len)]

    
    intent = "general"
    if any(word in question.lower() for word in ["symptom", "sign", "treatment", "diagnosis"]):
        intent = "symptoms"

    return intent, entities
