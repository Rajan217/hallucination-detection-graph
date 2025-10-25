from neo4j import GraphDatabase


URI = "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "Himanshu@321"

driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))

sections = ["Abstract", "Introduction", "Literature Review", "Methodology"]
entity_name = "Lung Cancer"

def create_graph(tx):
    
    tx.run("MERGE (e:Entity {name: $name})", name=entity_name)
    
    for section in sections:
        
        tx.run("MERGE (s:Section {name: $section})", section=section)
        
        tx.run("""
            MATCH (e:Entity {name: $entity_name}), (s:Section {name: $section})
            MERGE (e)-[r:MENTIONS]->(s)
            SET r.weight = 1.0
        """, entity_name=entity_name, section=section)

with driver.session() as session:
    session.execute_write(create_graph)

print(f"✅ Neo4j graph created: '{entity_name}' linked to all sections.")
driver.close()
