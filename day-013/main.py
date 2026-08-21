# Enunciado do exercício (dockerized fastapi)

# Crie a pasta day-013 com três arquivos:

# Um main.py com uma API FastAPI simples: uma rota GET em / retornando uma mensagem, e uma rota GET em /health retornando status ok (pode reaproveitar a lógica do day-005)
# Um Dockerfile que instale as dependências, copie o código, exponha a porta e suba o uvicorn

from fastapi import FastAPI

app = FastAPI(
    title="practice day 13",
    description="practing about fastapi and dockerfile together",
    version="1.0.0",
    contact={
        "name":"Lucas de Oliveira",
        "email":"lucasdeoliveira937@gmail.com"
    }
)

@app.get("/")
def hello_world():
    return {"Hello":"World"}

@app.get("/health")
def health_check():
    return {"status": "OK"}