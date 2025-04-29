from services.embedding_service import get_embedding
from services.vector_store import search_collection
import config

def search_knowledge_base(query):
    """
    Searches Weaviate for the best answer for the given math question.
    Returns a step-by-step solution if found, otherwise a fallback message.
    """
    # Generate embedding for user query
    query_vector = get_embedding(query)

    # Search Weaviate collection
    results = search_collection(query_vector, top_k=config.DEFAULT_SEARCH_TOP_K)

    if results:
        best_match = results[0]
        raw_answer = best_match.properties['answer']
        return f"✅ Step-by-step solution:\n\n{raw_answer}"
    else:
        return "❌ Sorry, I couldn't find a relevant answer in the knowledge base."

# Quick test (optional)
if __name__ == "__main__":
    sample_query = "What is the volume of a sphere?"
    response = search_knowledge_base(sample_query)
    print(response)
