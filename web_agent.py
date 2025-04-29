from tavily import TavilyClient
import config

client = TavilyClient(api_key=config.TAVILY_API_KEY)

def web_search(query):
    """
    Perform a web search using Tavily API.
    Returns the content of the top result.
    """
    try:
        results = client.search(query=query)
        top_result = results['results'][0]['content']
        return top_result
    except Exception as e:
        return f"Web search failed: {str(e)}"
