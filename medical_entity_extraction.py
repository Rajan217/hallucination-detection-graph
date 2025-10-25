import scispacy
import spacy

# Load SciSpacy medical NER model
nlp = spacy.load("en_ner_bc5cdr_md")

def extract_medical_entities(query):
    """
    Extract medical entities (diseases, chemicals) from a query.
    Returns a list of entities.
    """
    doc = nlp(query)
    entities = [ent.text for ent in doc.ents]
    return entities

# Example usage
if __name__ == "__main__":
    query = "What are the symptoms of lung cancer?"
    entities = extract_medical_entities(query)
    print("Extracted Medical Entities:", entities)
