
import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.Client()
collection = client.get_or_create_collection(name="medical_kb")
model = SentenceTransformer('all-MiniLM-L6-v2')

def add_info(text, text_id):
    vector = model.encode(text).tolist()
    collection.add(documents=[text], embeddings=[vector], ids=[text_id])

knowledge_items = [
    ("Paracetamol is used for fever and pain relief.", "med01"),
    ("Antibiotics do not work on viral infections like the cold.", "med02"),
    ("Keep a wound clean and covered to prevent infection.", "med03")
]

for text, id in knowledge_items:
    add_info(text, id)

def query_medical_kb(query):
    query_vector = model.encode(query).tolist()
    results = collection.query(query_embeddings=[query_vector], n_results=1)
    return results['documents'][0][0]

if __name__ == "__main__":
    print(f"Result: {query_medical_kb('fever medicine')}")
