import spacy
from utilis.file_utils import extract_text

nlp = spacy.load("en_core_web_sm")

def chunk(filepath, chunksize=3, overlap=1):
    text = extract_text(filepath)
    doc = nlp(text)
    texts = [sent.text for sent in doc.sents]

    chunks = []
    i = 0
    while i < len(texts):
        chunk_text = " ".join(texts[i:i+chunksize])
        if chunk_text:
            chunks.append(chunk_text)
        i += chunksize - overlap
    return chunks

  
