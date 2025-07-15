from nltk.tokenize import sent_tokenize
from utilis.file_utils import extract_text

def chunk(filepath, chunksize=500, overlap=50):
    text = extract_text(filepath)
    sentences = sent_tokenize(text)

    chunks = []
    i = 0
    while i < len(sentences):
        chunk_text = " ".join(sentences[i:i+chunksize])
        if chunk_text:
            chunks.append(chunk_text)
        i += chunksize - overlap
    return chunks

