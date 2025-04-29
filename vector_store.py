import weaviate
from weaviate.auth import AuthApiKey
import config

# Connect to Weaviate
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=config.WEAVIATE_ENDPOINT,
    auth_credentials=AuthApiKey(api_key=config.WEAVIATE_API_KEY),
)

def search_collection(query_vector, top_k=3):
    """
    Search the Weaviate MathQuestion collection using a vector.
    Returns top_k best matches.
    """
    collection = client.collections.get(config.VECTOR_DB_NAME)
    results = collection.query.near_vector(
        near_vector=query_vector,
        limit=top_k,
    )
    return results.objects

def upload_data(data):
    """
    Upload parsed knowledge base data into Weaviate.
    """
    collection = client.collections.get(config.VECTOR_DB_NAME)
    for item in data:
        collection.data.insert(
            properties={
                "question": item['question'],
                "answer": item['answer'],
            },
            vector=item['embedding']
        )
    print("✅ All data inserted successfully!")
