from sentence_transformers import SentenceTransformer

# Load the embedding model
model = SentenceTransformer('./local_model')  # Load from local path

def get_embedding(text):
    embedding = model.encode(text)
    return embedding.tolist()  # Return as a list
