# No test_weather.py:
# Um teste que usa monkeypatch (fixture embutida do pytest) pra substituir o requests.get por uma 
# função falsa que retorna uma resposta simulada com status 200 e um JSON de temperatura. 
# Verifique que sua função processa certo.
# Um teste que mocka uma resposta com status 404 e verifica que sua função retorna o erro.

import pytest
from weather import get_temperature

class FakeResponse:
    def __init__(self, json_data, status_code):
        self._json = json_data
        self.status_code = status_code
    def json(self):
        return self._json

def test_get_temperature_succes(monkeypatch):
    def fake_get(url):
        return FakeResponse({"temp": 25}, 200)
    monkeypatch.setattr("weather.requests.get", fake_get)
    
    result = get_temperature("London")
    assert result["temperature"] == 25

def test_get_temperature_not_found(monkeypatch):
    def fake_get(url):
        return FakeResponse({}, 404)
    monkeypatch.setattr("weather.requests.get", fake_get)
    
    result = get_temperature("Nowhere")
    assert result["message"] == "City's weather not found"