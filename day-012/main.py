# Enunciado do exercício (path params API)

# Crie day-012/main.py. A API deve ter:

# Uma rota GET em / com uma mensagem de boas-vindas (só pra ter a raiz)
# Uma rota GET em /users/{user_id} que receba um user_id inteiro e retorne um JSON com esse id
# Uma rota GET em /greet/{name} que receba um name (texto) e retorne uma saudação personalizada usando esse nome (exemplo: "Hello, Lucas")
# Uma rota GET em /square/{number} que receba um number inteiro e retorne o número e o quadrado dele

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def message_welcome():
    return {"message":"Welcome to my World"}

@app.get("/users/{user_id}", status_code=200)
def read_user(user_id: int):
    return {"user_id": user_id}

@app.get("/greet/{name}", status_code=200)
def read_name(name: str):
    return {"Hello": name}

@app.get("/square/{number}", status_code=200)
def read_number_square(number: int):
    square = number ** 2
    return {"number": number,
            "aquare": square}