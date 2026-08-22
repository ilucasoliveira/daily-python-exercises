# Enunciado (temperature converter API)

# Crie day-014/review_api.py. Uma API FastAPI que converte temperaturas. Deve ter:

# Uma rota GET em / com uma mensagem de boas-vindas em JSON
# Uma rota GET em /celsius/{value} que receba um value inteiro e retorne um JSON com a temperatura original em Celsius e o valor convertido para Fahrenheit. Fórmula: F = C * 9/5 + 32
# Uma rota GET em /fahrenheit/{value} que faça o caminho inverso, recebe Fahrenheit e retorna o valor em Celsius. Fórmula: C = (F - 32) * 5/9
# Em ambas, o JSON de resposta deve ter chaves claras e curtas (lembra da observação do day-012 sobre não usar frases inteiras como chave)

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def msg_welcome():
    return {"Hello":"Welcome!"}

@app.get("/celsius/{value}")
def celsius(value: int):
    fahrenheit = round(value * 9/5 + 32, 1)
    return {
        "celsius": value,
        "fahrenheit": fahrenheit
    }

@app.get("/fahrenheit/{value}")
def fahrenheit(value: int):
    celsius = round((value - 32) * 5/9, 1)
    return {
        "fahrenheit": value,
        "celsius": celsius
    }