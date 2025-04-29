from sentence_transformers import SentenceTransformer

# Load the embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')  # lightweight + powerful

def get_embedding(text):
    embedding = model.encode(text)
    return embedding.tolist()  # Return as a list
