import weaviate
from weaviate.auth import AuthApiKey
import config

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=config.WEAVIATE_ENDPOINT,
    auth_credentials=AuthApiKey(api_key=config.WEAVIATE_API_KEY),
)

# Check connection
if client.is_ready():
    print("✅ Successfully connected to Weaviate Cloud!")
else:
    print("❌ Failed to connect to Weaviate Cloud.")

# Close the connection properly
client.close()
