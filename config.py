import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Weaviate Cloud Details
WEAVIATE_ENDPOINT = os.getenv("WEAVIATE_ENDPOINT")
WEAVIATE_API_KEY = os.getenv("WEAVIATE_API_KEY")

# Vector Database Collection Name
VECTOR_DB_NAME = "MathQuestion"

# Embedding Model
EMBEDDING_MODEL = "text-embedding-ada-002"

# Tavily API Key (if you use Tavily for search later)
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Default Top-K value for vector search results
DEFAULT_SEARCH_TOP_K = 3
