import streamlit as st
from backend.chunker import chunk
from backend.embedder import get_embeddings
from backend.vector_store import addfiles, search_vector_store
from backend.retriever import callllm
import os
import spacy

# Download spaCy model if not already installed
spacy.cli.download("en_core_web_sm")

# Create upload directory if it doesn't exist
os.makedirs("data/uploads", exist_ok=True)

st.title("Chat with your Text/PDF File")

uploaded_file = st.file_uploader("Upload a text or PDF file", type=["txt", "pdf"])

chat_history = []

if uploaded_file:
    filepath = os.path.join("data/uploads", uploaded_file.name)
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())

    chunks = chunk(filepath)
    vectors = get_embeddings(chunks)
    addfiles(chunks, vectors, filepath)

    query = st.text_input(f"Ask something about: {uploaded_file.name}")

    if query:
        results = search_vector_store(query)
        context = "\n\n".join(results["documents"][0])

        history_text = "\n".join([
            f"User: {turn['user']}\nAssistant: {turn['ai']}" for turn in chat_history
        ])

        prompt = f"""You are a smart AI assistant.

Context:
{context}

Chat history:
{history_text}

Question:
{query}

Answer:"""

        answer = callllm(prompt)
        chat_history.append({"user": query, "ai": answer})

        final_output = f"""
**Answer:** {answer}

**Sources:**  - {results['metadatas'][0]}
"""
        st.markdown(final_output)
