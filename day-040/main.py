# Enunciado (github user cache)

# Crie a pasta day-040. Um sistema que busca dados de um usuário do GitHub (a API que você usou no day-036, sem precisar de chave) 
# e cacheia no Redis. Tudo tipado, com funções separadas.
# Precisa do Redis rodando (docker run -d -p 6379:6379 --name redis-cache redis:alpine, ou reaproveita o que já subiu)
# e das libs (pip install requests redis python-dotenv).

# O programa deve:
# Uma função fetch_user(username: str) -> dict que:
# chame a API do GitHub (https://api.github.com/users/{username})
# verifique o status (404 vira erro tratado)
# retorne um dicionário com campos escolhidos (name, public_repos, followers)
# trate falha de conexão com RequestException
# retorno sempre dict, com type hint
# Uma função get_user_cached(username: str) -> dict com cache-aside:
# olha no Redis primeiro (get)
# se achou, retorna sinalizando origem cache (json.loads)
# se não, chama fetch_user, guarda no Redis com set(..., ex=TTL) e retorna sinalizando origem api
# importante: só cacheie se NÃO for erro (não guarde no Redis um resultado que tem a chave "error", lembra da reflexão do day-039)
# No corpo principal:
# chame get_user_cached pro mesmo usuário DUAS vezes (primeira api, segunda cache)
# chame pra um usuário que não existe e mostre o erro tratado (e confirme que ele NÃO foi cacheado)

# Conceito bônus opcional (se quiser desafio): adicione uma função que mostra o TTL restante de uma chave no Redis, 
# com redis_client.ttl(username). Retorna quantos segundos faltam pro cache expirar. Mostra o cache "vivo".
import json
import redis
import requests

redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)

def fetch_user(username: str) -> dict:
    try:
        response = requests.get(f"https://api.github.com/users/{username}")
        if response.status_code != 200:
            return {"error": "username not found or invalid"}
        data = response.json()
        return {
            "name": data["name"],
            "public_repos": data["public_repos"],
            "followers": data["followers"]
        }
    except requests.exceptions.RequestException as e: 
        return {"error": str(e)}

def get_user_cached(username: str) -> dict:
    
    cached = redis_client.get(username)
    if cached:
        return {
            "source": "redis",
            "data": json.loads(cached)
        }
    
    data = fetch_user(username)
    
    if "error" not in data:
        redis_client.set(username, json.dumps(data), ex=300)
    
    return {
        "source": "API",
        "data": data
    }

print(get_user_cached("ilucasoliveira"))
print(get_user_cached("ilucasoliveira"))

print(get_user_cached("user_wrong@#123"))
