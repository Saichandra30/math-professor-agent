import weaviate
from weaviate.auth import AuthApiKey
import config
from weaviate.collections.classes.config import Property, DataType, Configure

# Connect to Weaviate
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=config.WEAVIATE_ENDPOINT,
    auth_credentials=AuthApiKey(api_key=config.WEAVIATE_API_KEY),
)

def create_schema():
    """
    Create the MathQuestion collection in Weaviate if it does not already exist.
    """
    existing_collections = client.collections.list_all().keys()

    if config.VECTOR_DB_NAME in existing_collections:
        print(f"✅ Collection '{config.VECTOR_DB_NAME}' already exists!")
        return

    # Create new collection
    client.collections.create(
        name=config.VECTOR_DB_NAME,
        properties=[
            Property(name="question", data_type=DataType.TEXT),
            Property(name="answer", data_type=DataType.TEXT),
        ],
        vectorizer_config=Configure.Vectorizer.none()
    )

    print(f"✅ Collection '{config.VECTOR_DB_NAME}' created successfully!")

if __name__ == "__main__":
    create_schema()
    client.close()