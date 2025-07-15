#RAG Chat with Your Documents

Upload any `.pdf` or `.txt` document and chat with it using advanced Retrieval-Augmented Generation (RAG). This project uses embeddings, vector search, and large language models (LLMs) to generate smart answers from your own documents.

---

 Features

-  Upload `.pdf` and `.txt` files
-  Extract text and split into overlapping chunks
-  Generate sentence embeddings using Sentence Transformers
-  Store and search vectors using ChromaDB
-  Use Groq LLM (Mixtral) to answer queries with retrieved context
-  Memory support for chat history
-  Simple UI with Streamlit

---

# Project Structure

rag-chat-documents/
│
├── app.py # Main Streamlit app
├── requirements.txt # Required Python packages
├── backend/
│ ├── chunker.py # Splits extracted text into chunks
│ ├── embedder.py # Embeds the text chunks
│ ├── retriever.py # Calls the LLM (Groq)
│ ├── vector_store.py # Stores and queries the vector DB
│ 
├── utilis/
│ ├── file_utils.py # Extracts text from txt/pdf
│ └── config.py # Environment variables or config
├── data/
│ ├── uploads/ # Uploaded files go here
│ └── vector_db/ # ChromaDB vector storage
├── README.md
└── .gitignore

 Setup Instructions

 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/rag-chat-documents.git
cd rag-chat-documents
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py

Tech Stack
Sentence Transformers for embedding text

ChromaDB for storing and querying vectors

Groq (Mixtral LLM) as the language model

Streamlit for the frontend UI

PyMuPDF for parsing PDFs

nltk for sentence splitting
