# Um test_main.py com testes usando TestClient:
# testar que a rota / retorna status 200 e a mensagem certa
# testar que /items/5 retorna status 200 e o id 5
# testar que /items/abc (id inválido) retorna status 422 (validação automática)
# testar que o POST /items com dados válidos retorna 201 e o item
# testar que o POST /items com dados inválidos (faltando campo ou tipo errado) retorna 422
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root_greeting():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message":"Welcome!"}

def test_read_root_items_id():
    response = client.get("/items/10")
    assert response.status_code == 200
    assert response.json() == {"id": 10}

def test_read_root_items_id_error():
    response = client.get("/items/abc")
    assert response.status_code == 422

def test_create_root_items():
    response = client.post("/items", json={"name": "apple", "price": 3.15})
    assert response.status_code == 201
    assert response.json() == {
        "message": "Item Created",
        "name": "apple",
        "price": 3.15}

def test_create_root_items_error():
    response = client.post("/items", json={"name": "apple"})
    assert response.status_code == 422
