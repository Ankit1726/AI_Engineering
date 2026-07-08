from langchain_core.tools import tool 
import os,requests,sqlite3,math

@tool
def calculator(expression: str) -> str:
    """
    Useful for performing simple mathematical calculations.

    Input should be a valid mathematical expression.
    Examples:
    - 2 + 2
    - math.sqrt(16)
    - 10 * 5
    """
    try:
        allowed = {
            "math": math,
            "abs": abs,
            "round": round,
            "min": min,
            "max": max,
            "sum": sum,
        }

        result = eval(expression, {"__builtins__": {}}, allowed)
        return str(result)

    except Exception as e:
        return f"Calculation error: {e}"
    
@tool
def get_stock_price(symbol: str) -> dict:
    """
    Fetch the latest stock price for a given stock symbol.
    Example: AAPL, TSLA, MSFT
    """
    try:
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={os.getenv('ALPHA_VANTAGE_API_KEY')}"
        response = requests.get(url)
        return response.json()
    except Exception as e:
        return {"error": str(e)}
    
@tool
def get_current_weather(location: str) -> str:
    """
    Get the current weather for a city.
    Example: Delhi, London, New York
    """
    try:
        api_key = os.getenv("OPENWEATHER_API_KEY")

        url = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            "q": location,
            "appid": api_key,
            "units": "metric"
        }

        data = requests.get(url, params=params).json()

        if data.get("cod") != 200:
            return f"Weather not found for {location}."

        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        return (
            f"Weather in {location}: {weather.title()}, "
            f"Temperature: {temp}°C, Humidity: {humidity}%."
        )

    except Exception as e:
        return f"Error: {e}"