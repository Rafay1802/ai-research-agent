import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

def web_search(query: str) -> str:
    """Search the web for current information on any topic."""
    client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    results = client.search(query, max_results=5)
    
    output = ""
    for r in results["results"]:
        output += f"Title: {r['title']}\nURL: {r['url']}\nSummary: {r['content']}\n\n"
    return output

tools_list = [
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Search the web for current information on any topic",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query"
                    }
                },
                "required": ["query"]
            }
        }
    }
]