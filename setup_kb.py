import json
import config
import weaviate
from weaviate.auth import AuthApiKey

from services.embedding_service import get_embedding

# Connect to Weaviate Cloud (new method)
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=config.WEAVIATE_ENDPOINT,
    auth_credentials=AuthApiKey(api_key=config.WEAVIATE_API_KEY),
)

# Load your knowledge base (new file)
with open("data/parsed_math_knowledge.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Get the collection object
collection = client.collections.get(config.VECTOR_DB_NAME)

# Upload each item
for item in data:
    question = item["question"]
    answer = item["answer"]
    embedding = get_embedding(question)

    # Insert into Weaviate
    collection.data.insert(
        properties={
            "question": question,
            "answer": answer,
        },
        vector=embedding
    )

print("✅ Knowledge base uploaded successfully!")

# Close connection (good practice)
client.close()
