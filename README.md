# Hallucination Detection using Graph and Vector-based Scores

This project detects **AI hallucinations** in responses by combining **Graph-based**, **Vector-based**, and **Unified scoring** techniques.  
It helps identify whether an AI-generated answer is **factually grounded** or **hallucinated** based on similarity and knowledge graph analysis.

---

## Features
- Calculates **Graph-based Score** using relationships between entities in a Neo4j graph.
- Computes **Vector-based Score** using text embeddings and cosine similarity.
- Combines both into a **Unified Score** using weighted average.
- Normalizes results for better comparison across multiple queries.
- Accepts **any user question dynamically** (e.g., *"What are the symptoms of lung cancer?"*).

---

##  Project Structure

graph/
│
├── create_neo4j_graph.py # Creates the medical knowledge graph in Neo4j
├── populate_neo4j.py # Loads entities and relations into Neo4j
├── medical_entity_extraction.py # Extracts entities from text
├── vector_layer.py # Handles vector embeddings and similarity
├── graph_layer.py # Handles graph-based scoring
├── unified_layer.py # Combines both scores with weighting
├── score_system.py # Calculates and normalizes unified score
├── example_run_unified.py # Main entry to run the project
├── documents.json # Dataset for knowledge and testing
├── requirements.txt # Dependencies
├── .gitignore # Ignored files (e.g., venv)
└── README.md # Project documentation

yaml
Copy code

---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Rajan217/hallucination-detection-graph.git
cd hallucination-detection-graph
2️⃣ Create virtual environment
bash
Copy code
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate   # On Linux/Mac
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Set up Neo4j
Install Neo4j Desktop

Run a local database and note the URI, username, and password.

Update them in your code where required.

▶️ How to Run
Run the main script:

bash
Copy code
python example_run_unified.py
Then, enter any question such as:

sql
Copy code
What are the symptoms of lung cancer?
You’ll get output like:

yaml
Copy code
Graph Score: 1.5
Vector Score: 0.4471
Unified Score: 1.0788
Normalized Unified Score: 0.9256
🧮 Scoring Logic
Score Type	Description	Range
Graph Score	Measures entity and relationship relevance in Neo4j	0 - 3
Vector Score	Uses cosine similarity between user query and documents	0 - 1
Unified Score	Weighted sum of Graph & Vector scores	Dynamic
Normalized Score	Unified score scaled to 0–1	0 - 1

Weights Example:

Graph Weight = 0.6

Vector Weight = 0.4
You can modify these in unified_layer.py.

📊 Example Output
Question	Graph Score	Vector Score	Unified Score	Normalized Score
What are the symptoms of lung cancer?	1.5	0.4471	1.0788	0.9256
How is diabetes treated?	2.3	0.6210	1.789	0.964

💡 Future Enhancements
Add a web interface using Streamlit or React + Flask.

Integrate Wikipedia / PubMed for real-time factual grounding.

Deploy model to Hugging Face Spaces or Render.

👨‍💻 Author
Rajan Pandit


