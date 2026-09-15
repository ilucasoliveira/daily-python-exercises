from main import get_weather

class FakeResponse:
    def __init__(self, json_data, status_code):
        self._json = json_data
        self.status_code = status_code
    def json(self):
        return self._json

def test_get_weather_success(monkeypatch):
    fake_data = {
        "name": "London",
        "main": {"temp": 15.5},
        "weather": [{"description": "cloudy"}]
    }
    
    def fake_get(url, params=None):
        return FakeResponse(fake_data, 200)
    monkeypatch.setattr("main.requests.get", fake_get)
    
    result = get_weather("London")
    assert result["temp"] == 15.5

def test_get_weather_not_found(monkeypatch):
    def fake_get(url, params=None):
        return FakeResponse({}, 404)
    monkeypatch.setattr("main.requests.get", fake_get)
    
    result = get_weather("InexistentCity")
    assert "not found" in result["error"]