# Enunciado do exercício (first API)

# Crie a pasta day-005 e, dentro dela, o arquivo main.py. A API deve ter:

# Uma rota GET em / que retorna uma mensagem de boas-vindas em JSON
# Uma rota GET em /about que retorna um JSON com pelo menos 2 informações suas (exemplo: name e role)
# Uma rota GET em /health que retorna {"status": "ok"}

from fastapi import FastAPI

app = FastAPI(
    title="practicing-with-FastAPI",
    description="day 05 practicing about FastAPI",
    version="1.0.0",
    contact={
        "name":"Lucas de Oliveira",
        "email":"lucasdeoliveira937@gmail.com"
    }
)

@app.get("/")
def welcome_msg():
    return {"message": "Welcome to my world"}

@app.get("/about")
def read_me():
    return {
        "name":"Lucas de Oliveira",
        "profession":"Full-Stack Python Developer"
    }

@app.get("/health")
def health_check():
    return {"status": "OK"}