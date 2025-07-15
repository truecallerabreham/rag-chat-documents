import streamlit as st
import spacy
import os

from backend.chunker import chunk
from backend.embedder import get_embeddings
from backend.vector_store import addfiles, search_vector_store
from backend.retriever import callllm

# Ensure upload directory exists
os.makedirs("data/uploads", exist_ok=True)

st.title("Chat with your Text/PDF File")

uploaded_file = st.file_uploader("Upload a text or PDF file", type=["txt", "pdf"])

chat_history = []

if uploaded_file:
    # Save uploaded file
    filepath = os.path.join("data/uploads", uploaded_file.name)
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Chunk the file
    chunks = chunk(filepath)

    # Embed chunks
    vectors = get_embeddings(chunks)

    # Store in vector DB
    addfiles(chunks, vectors, filepath)

    # Get query from user
    query = st.text_input(f"Ask something about: {uploaded_file.name}")

    if query:
        # Search DB
        results = search_vector_store(query)
        context = "\n\n".join(results["documents"][0])

        # Format chat history
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

        # Call the LLM
        answer = callllm(prompt)

        # Update memory
        chat_history.append({"user": query, "ai": answer})

        # Show final output
        st.markdown(f"""
**Answer:** {answer}

**Sources:** - {results['metadatas'][0]}
""")
