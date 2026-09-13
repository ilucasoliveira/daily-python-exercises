# Enunciado (mocked api tests)
# Crie a pasta day-036 (ou adiciona): weather.py e test_weather.py.

# No weather.py:
# Uma função get_temperature(city: str) -> dict que (simuladamente) buscaria o clima de uma cidade numa API. 
# Pra manter simples e testável, ela recebe também um parâmetro de conexão, OU você estrutura assim: a função 
# faz requests.get(url), checa status, e retorna um dicionário com a cidade e a temperatura extraída do JSON. Se status não for 200, retorna erro.

import requests

def get_temperature(city: str) -> dict:
    
    response = requests.get(f"https://fake-weather.com/{city}")
    if response.status_code != 200:
        return {"message":"City's weather not found"}
    
    data = response.json()
    
    return {"city": city, "temperature": data["temp"]}