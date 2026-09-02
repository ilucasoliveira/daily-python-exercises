# Enunciado do exercício (compose with redis)

# Crie a pasta day-025 com estes arquivos:

# Um main.py com uma API FastAPI que conecte no Redis e use ele de forma simples: uma rota 
# que incrementa um contador no Redis a cada acesso e retorna o valor atual. Exemplo de lógica: 
# a rota / chama redis.incr("counter") e retorna o número. Isso prova que a API está falando com o Redis.
# Um requirements.txt (ou pyproject, como preferir) incluindo fastapi, uvicorn e redis
# Um Dockerfile pra API (pode reaproveitar a estrutura do day-013)
# Um docker-compose.yml com os dois serviços: api e redis

import redis
from fastapi import FastAPI

redis_client = redis.Redis(host="redis", port=6379, db=0, decode_responses=True)

app = FastAPI()

@app.get("/")
def count_visits():
    total = redis_client.incr("counter")
    return {"visits": total}