from sentence_transformers import SentenceTransformer
import os

# Load model from local folder (no internet needed)
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'local_model')
model = SentenceTransformer(MODEL_PATH)

def get_embedding(text):
    return model.encode(text).tolist()
