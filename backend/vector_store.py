import chromadb
from chromadb.config import Settings

client = chromadb.PersistentClient(path="data/vector_db")

collection = client.get_or_create_collection(name="my_collection")

def addfiles(chunks, vectors, filepath):
    collection.add(
        documents=chunks,
        ids=[f"chunk{i}" for i in range(len(chunks))],
        embeddings=vectors,
        metadatas=[{"source": filepath}] * len(chunks)
    )

def search_vector_store(query, k=3):
    results = collection.query(
        query_texts=[query],
        n_results=k
    )
    return results
