// constraints / indexes
CREATE CONSTRAINT IF NOT EXISTS FOR (d:Document) REQUIRE d.id IS UNIQUE;
CREATE CONSTRAINT IF NOT EXISTS FOR (e:Entity) REQUIRE e.name IS UNIQUE;


MERGE (d1:Document {id: "docA", title: "Lung Cancer Symptoms", text:"Persistent cough, chest pain..."})
MERGE (d2:Document {id: "docB", title: "Lung Cancer Diagnosis", text:"Imaging, biopsy..."})

// sample entities
MERGE (e1:Entity {name: "Lung Cancer"})
MERGE (e2:Entity {name: "Persistent Cough"})
MERGE (e3:Entity {name: "Biopsy"})

// relationships (weights on edges)
MERGE (e1)-[:MENTIONS {weight: 1.0}]->(d1)
MERGE (e2)-[:MENTIONS {weight: 0.8}]->(d1)
MERGE (e3)-[:MENTIONS {weight: 0.6}]->(d2)
MERGE (e1)-[:RELATED {weight: 0.9}]->(e2)
