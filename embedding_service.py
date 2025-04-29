from sentence_transformers import SentenceTransformer

model = SentenceTransformer('./local_model')  # Local model

def get_embedding(text):
    return model.encode(text).tolist()
