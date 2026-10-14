import requests
from langchain_core.tools import tool

from langchain_community.tools.tavily_search import TavilySearchResults


@tool
def get_stock_info(symbol: str) -> dict:
    """
        Fetches the latest stock news and information.
    
    
        Args:
            HIVE
        
    """
    

    url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE"
    
    # Specify the trading pair (Bitcoin to Tether USD)
    params = {"symbol": symbol, "apikey": "#"}

    response = requests.get(url, params=params)
    data = response.json()
    print(data)
    return data

@tool
def get_city_news(city:str) -> list[dict]:
    """
    Fetches the latest news articles for a specified city.


    Args:
        city: The name of the city to search news for.
    
    """


    search_tool = TavilySearchResults(
        tavily_api_key = "#",
        topic = "news",
        max_results = 5,
        search_depth = "advanced",
        include_images=False

    )
    query = f"Latest breaking and important news and events in {city} city"


    return search_tool.invoke({
        "query":query
    })



