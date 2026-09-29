# Enunciado do exercício (async api gateway)
# Crie a pasta day-052 com main.py. Instale: pip install fastapi uvicorn httpx. Uma API que consome a jsonplaceholder de forma assíncrona. O programa deve ter:

# Uma rota GET /users/{user_id} (async) que busque um usuário na jsonplaceholder (https://jsonplaceholder.typicode.com/users/{user_id}) 
# de forma assíncrona e retorne alguns campos (name, email, city que fica em address.city). Trate o caso de não encontrar (status != 200).
# Uma rota GET /users/{user_id}/posts (async) que busque os posts daquele usuário (https://jsonplaceholder.typicode.com/posts?userId={user_id})
# e retorne quantos posts ele tem e os títulos.
# # Uma rota GET /dashboard/{user_id} (async) que junte as duas coisas AO MESMO TEMPO com asyncio.gather: busca o usuário E os posts dele
# em paralelo, e retorna tudo num JSON só. Esse é o ponto alto: duas buscas externas em paralelo dentro de uma rota.
import httpx
import asyncio

from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="day-052: async api gateway",
    version="0.1.0",
    contact={
        "name": "Lucas de Oliveira Pimentel",
        "email": "lucasoliveirapimentel.dev@gmail.com"
    }
)

@app.get("/health")
def health_check():
    return {"status": "OK"}

@app.get("/users/{user_id}", status_code=200, tags=["user"])
async def get_user(user_id: int) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="user not found")
        data = response.json()
    return {
        "name": data.get("name"),
        "email": data.get("email"),
        "city": data["address"]["city"]
    }

@app.get("/users/{user_id}/posts", status_code=200, tags=["user"])
async def get_user_posts(user_id: int) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://jsonplaceholder.typicode.com/posts?userId={user_id}")
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="user not found")
        data = response.json()
    return {
        "posts_quantity": len(data),
        "titles": [f"{i + 1} - {title['title']}" for i, title in enumerate(data)]
    }

@app.get("/dashboard/{user_id}", status_code=200, tags=["user"])
async def get_parallel(user_id: int) -> dict:
    user_data, post_data = await asyncio.gather(
        get_user(user_id),
        get_user_posts(user_id)
    )
    return {
        "user": user_data,
        "posts": post_data
    }


