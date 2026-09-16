# Enunciado do exercício (weather cache)
# Crie a pasta day-039. Reaproveite a lógica de clima do day-038. O programa deve:

# Conectar no Redis (redis.Redis(host="localhost", port=6379, decode_responses=True))
# Uma função get_weather_cached(city: str) -> dict que implemente o cache-aside:
# primeiro tenta pegar do Redis com r.get(city)
# se achou (cache hit), retorna o dado (lembra do json.loads) e de alguma forma sinaliza que veio do cache 
# (exemplo: adiciona uma chave "source": "cache" ou imprime "from cache")
# se não achou (cache miss), chama a API real (sua get_weather do day-038), guarda no Redis com setex e um TTL 
# (exemplo 300 segundos), e retorna sinalizando que veio da API
# No corpo principal, chame get_weather_cached pra mesma cidade DUAS vezes seguidas. A primeira deve ir na API 
# (cache miss), a segunda deve vir do cache (cache hit). Imprima as duas, mostrando a diferença na origem.
import os
import json
import redis
import requests

from dotenv import load_dotenv

load_dotenv()
WEATHER_API = os.getenv("WEATHER_API_KEY")

redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)

def get_weather(city: str) -> dict:
    try:
        params = {
            "q":city,
            "appid":WEATHER_API,
            "units":"metric"
            }
        response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
        if response.status_code != 200:
            return {"error": "city not found or invalid name"}
        data = response.json()
        return {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def get_weather_cached(city: str) -> dict:
    cached = redis_client.get(city)
    if cached:
        return {
            "source": "redis",
            "data": json.loads(cached)
            }
    
    data = get_weather(city)
    redis_client.set(city, json.dumps(data), ex=300)
    return {
        "source": "API",
        "data": data
        }

print(get_weather_cached("Barbacena"))
print(get_weather_cached("Barbacena"))