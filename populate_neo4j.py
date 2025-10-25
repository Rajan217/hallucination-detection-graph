from neo4j import GraphDatabase

# Neo4j connection settings
uri = "bolt://localhost:7687"
user = "neo4j"
password = "Himanshu@321"

driver = GraphDatabase.driver(uri, auth=(user, password))

# Your JSON sections
documents = {
    "Abstract": "In recent times, Lung cancer is the most common cause of mortality in both men and women around the world. Lung cancer is the second most well-known disease after heart disease. Although lung cancer prevention is impossible, early detection of lung cancer can effectively treat lung cancer at an early stage. The possibility of a patient's survival rate increasing if lung cancer is identified early. To detect and diagnose lung cancer in its early stages, a variety of data analysis and machine learning techniques have been applied. In this paper, we applied supervised machine learning algorithms like SVM (Support vector machine), ANN (Artificial neural networks), MLR (Multiple linear regression), and RF (random forest), to detect the early stages of lung tumors. The main purpose of this study is to examine the success of machine learning algorithms in detecting lung cancer at an early stage. When compared to all other supervised machine learning algorithms, the Random forest model produces a high result, with a 99.99% accuracy rate.",
    "Methodology": "This study focuses on early detection of lung cancer using machine learning techniques. Four classifiers—ANN, SVM, Random Forest, and Multiple Linear Regression—are applied to a lung cancer dataset to determine the most accurate model."
}

# Entity to connect
entities = ["lung cancer"]

with driver.session() as session:
    # Create entity nodes
    for e in entities:
        session.run("""
        MERGE (ent:Entity {name: $name})
        """, {"name": e})

    # Create document nodes and connect to entity
    for doc_id, text in documents.items():
        session.run("""
        MERGE (d:Document {id: $doc_id})
        SET d.text = $text
        """, {"doc_id": doc_id, "text": text})

        # Connect entity to document with weighted relationship
        for e in entities:
            session.run("""
            MATCH (ent:Entity {name: $entity_name}), (d:Document {id: $doc_id})
            MERGE (ent)-[r:MENTIONS]->(d)
            ON CREATE SET r.weight = 1.0
            """, {"entity_name": e, "doc_id": doc_id})

print("Neo4j graph populated successfully with entities and documents!")
driver.close()
