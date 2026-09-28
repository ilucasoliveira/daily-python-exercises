# (review extra) consumir várias APIs em paralelo com async

# Tema: requisições HTTP assíncronas, buscar de vários lugares ao mesmo tempo
# O conceito que isso mostra: no day-36/40 você buscava usuários do GitHub um de cada vez (síncrono). 
# Se você busca 5 usuários, são 5 esperas em sequência. Com async, você dispara as 5 requisições juntas e espera todas ao mesmo tempo. 
# Numa API real que agrega dados de vários serviços, isso é a diferença entre lento e rápido.

# Enunciado (async api fetch)
# Crie day-051/review.py. Instale se precisar: pip install httpx. O programa deve:
# Uma corotina fetch_user(client, username) que use o httpx.AsyncClient pra buscar um usuário do GitHub 
# (https://api.github.com/users/{username}) de forma assíncrona (com await), e retorne o nome e o número de repos (ou um erro se falhar).
# Uma corotina fetch_all_sync_style(usernames) que busque os usuários UM DE CADA VEZ (com await em sequência, sem gather) e meça o tempo. Isso simula o jeito lento.
# Uma corotina fetch_all_parallel(usernames) que busque TODOS ao mesmo tempo com asyncio.gather e meça o tempo. Esse é o jeito rápido.
# No main(), rode as duas versões com a mesma lista de uns 4-5 usernames reais (ex: torvalds, gvanrossum, etc.) 
# e imprima os dois tempos, mostrando que o paralelo é bem mais rápido.
import httpx
import asyncio
import time

async def fetch_user(client: httpx.AsyncClient, username: str) -> dict:
    try: 
        response = await client.get(f"https://api.github.com/users/{username}")
        if response.status_code != 200:
            return {"error": "username not found"}
        data = response.json()
        return {
        "name": data.get("name"),
        "repos": data.get("public_repos")
        }
    except httpx.HTTPError as e:
        return {"error": str(e)}

async def fetch_all_sync_style(usernames) -> list:
    async with httpx.AsyncClient(headers={"User-Agent": "meu-app"}) as client:
        results = []
        for username in usernames:
            user = await fetch_user(client, username)
            results.append(user)
    return results

async def fetch_all_parallel(usernames):
    async with httpx.AsyncClient(headers={"User-Agent": "meu-app"}) as client:
        results = await asyncio.gather(*[fetch_user(client, username) for username in usernames])
    return results

users_list = ["ilucasoliveira", "lucascanton", "ottaviorr", "torvalds", "gvanrossum"]

async def main():
    start = time.perf_counter()
    sequential_results = await fetch_all_sync_style(users_list)
    finish = time.perf_counter()
    print(f"Sequential: {finish - start:.2f}s")
    
    parallel_start = time.perf_counter()
    parallel_results = await fetch_all_parallel(users_list)
    parallel_finish = time.perf_counter()
    print(f"Parallel: {parallel_finish - parallel_start:.2f}s")
    
    for user in parallel_results:
        print(user)

asyncio.run(main())
