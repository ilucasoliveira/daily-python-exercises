import os
import requests

from dotenv import load_dotenv

load_dotenv()
WEATHER_API = os.getenv("WEATHER_API_KEY")

def get_weather(city: str) -> dict:
    try:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {"q":city, "appid":WEATHER_API, "units":"metric"}
        response = requests.get(url, params=params)
        
        if response.status_code != 200:
            return {"error": f"{city} not found or invalid key"}
        
        data = response.json()
        return {
                "city": data["name"],
                "temp": data["main"]["temp"],
                "description": data["weather"][0]["description"]
            }
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

print(get_weather("Barbacena"))
print(get_weather("Belo Horizonte"))