# Um main.py com uma API FastAPI pequena e totalmente tipada:
# um modelo Pydantic Item com name: str e price: float
# uma rota GET / que retorne uma mensagem de boas-vindas
# uma rota GET /items/{item_id} tipada (item_id: int) que retorne o id recebido
# uma rota POST /items que receba um Item e retorne ele com uma mensagem (status 201)
from fastapi import FastAPI
from pydantic import BaseModel, Field

class SchemaItem(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    price: float = Field(ge=0)

class SchemaItemResponse(BaseModel):
    message: str
    name: str
    price: float

app = FastAPI()

@app.get("/")
def greeting():
    return {"message":"Welcome!"}

@app.get("/items/{item_id}")
def show_id_item(item_id: int) -> dict:
    return {"id": item_id}

@app.post("/items", status_code=201, response_model=SchemaItemResponse)
def create_item(item: SchemaItem) -> dict:
    return {
        "message": "Item Created",
        "name": item.name,
        "price": item.price
    }
