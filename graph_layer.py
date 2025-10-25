from neo4j import GraphDatabase

class GraphLayer:
    def __init__(self, uri="bolt://localhost:7687", user="neo4j", password="Himanshu@321"):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))



    def close(self):
        self.driver.close()

    def compute_connectivity_score(self, entity_name, doc_id):
        """
        Compute score based on:
        - Number of paths between entity and document
        - Lengths of paths (shorter paths → higher score)
        - Weights of relationships along paths
        Returns a float score between 0 and 1
        """
        with self.driver.session() as session:
            result = session.run(
                """
                MATCH (e:Entity {name: $entity_name}), (d:Document {id: $doc_id})
                OPTIONAL MATCH path = (e)-[rels*1..3]->(d)
                RETURN collect(path) AS paths
                """,
                entity_name=entity_name,
                doc_id=doc_id
            )

            record = result.single()
            paths = record["paths"] if record else []

            if not paths:
                return 0.0

            # Compute score per path: weight / length
            scores = []
            for p in paths:
                length = len(p)
                weight = 1.0
                for r in p.relationships:
                    weight *= r.get("weight", 1.0)
                scores.append(weight / length)  # shorter paths = higher score

            # Sum all path scores
            total_score = sum(scores)
            return total_score
