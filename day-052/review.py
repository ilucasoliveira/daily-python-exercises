# Enunciado (batch dashboard)

# Crie day-052/review.py. Uma API FastAPI que agrega dados de múltiplos usuários da jsonplaceholder ao mesmo tempo. O programa deve ter:

# Uma corotina auxiliar fetch_user_summary(client, user_id) que busque um usuário e retorne um resumo (name, email, e a quantidade de posts 
# dele buscando /posts?userId={id}). Repara: dentro dela você faz DUAS buscas (o usuário e os posts). Pra ganhar tempo, pode até fazer essas 
# duas com gather também, mas não é obrigatório.
# Uma rota GET /batch?ids=1,2,3 (async) que receba uma lista de ids e busque o resumo de TODOS eles em paralelo com asyncio.gather, retornando 
# a lista de resumos. Dica pra receber a lista: use um query parameter que vem como string ("1,2,3") e você separa com .split(",").
# Meça o tempo dentro da rota e inclua na resposta (quanto levou pra buscar todos). Compare mentalmente: se fosse sequencial, seria a soma; 
# com gather, é o tempo do mais lento.
import httpx
import asyncio
import time
from fastapi import FastAPI, HTTPException

app = FastAPI()

async def fetch_user_summary(client, user_id: int) -> dict:
    user_response = await client.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    posts_response = await client.get(f"https://jsonplaceholder.typicode.com/posts?userId={user_id}")
    if user_response.status_code != 200 or posts_response.status_code != 200:
        raise HTTPException(status_code=404, detail="user not found")
    user_data = user_response.json()
    posts_data = posts_response.json()
    return {
        "name": user_data.get("name"),
        "email": user_data.get("email"),
        "posts": {
            "quantity": len(posts_data),
            "titles": [i.get("title") for i in posts_data] 
        }
    }

@app.get("/batch", status_code=200)
async def get_multiple_users(ids: str) -> dict:
    id_list = [int(i) for i in ids.split(",")]
    async with httpx.AsyncClient() as client:
        start = time.perf_counter()
        results = await asyncio.gather(
            *[fetch_user_summary(client, user_id) for user_id in id_list]
        )
        finish = time.perf_counter()
        print(finish - start)
    return {"users": results}