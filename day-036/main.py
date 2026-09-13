# Enunciado do exercício (api consumer)
# Crie a pasta day-036 com main.py. Instale o requests antes:
# pip install requests

# O programa deve usar uma API pública e gratuita que não exige autenticação. Sugestão: a própria API do GitHub (https://api.github.com/users/USERNAME), 
# que retorna dados públicos de um usuário. O programa deve:

# Uma função get_user(username: str) -> dict que faça uma requisição à API do GitHub pra um usuário e retorne os dados como dicionário. 
# Trate o caso de erro: se o status não for 200, retorne um dicionário com uma mensagem de erro (use try/except também).
# No corpo principal, chame a função com um username real (exemplo: "torvalds" ou o seu, "ilucasoliveira") e imprima alguns campos 
# do retorno: nome, número de repositórios públicos (public_repos), seguidores (followers).
# Teste também com um username que não existe (tipo "esse_user_nao_existe_12345") e veja o tratamento de erro funcionar.

# Critério de pronto: a função faz a requisição, converte o JSON, trata o caso de erro (status diferente de 200 ou exceção),
# e o corpo principal mostra dados reais de um usuário. Mais pelo menos 1 commit.

# Como testar
# python day-036/main.py
# Você precisa de internet pra rodar (a API é externa). Confere você mesmo: ao buscar um usuário que existe, aparecem os
# dados reais dele? E ao buscar um que não existe, o tratamento de erro age em vez de quebrar?

# Mensagem de commit sugerida
# day-036: consuming external apis with requests
# Antes de codar, me confirma dois pontos: o que o .json() faz com a resposta de uma requisição? E por que é 
# importante verificar o status_code antes de usar os dados de uma API externa?
import requests

def get_user(username: str) -> dict:
    
    try:
        response = requests.get(f"https://api.github.com/users/{username}")
        if response.status_code !=  200:
            return {"message":"ERROR! User not found"}
        data = response.json()
    except ValueError as v:
        return {"ERROR": str(v)}
    except TypeError as t:
        return {"ERROR": str(t)}
    
    return {
        "name": data["name"],
        "location": data["location"],
        "created_at": data["created_at"]
    }

def data_print(username):
    print(get_user(username))

data_print("ilucasoliveira")
data_print("lucascanton")

data_print("user_234252_error")

