# Enunciado do exercício (post and headers)

# Crie a pasta day-037 com main.py. Vamos usar a httpbin.org, 
# uma API pública feita pra testar requisições (ela devolve de volta o que você enviou, ótima pra aprender). O programa deve:

# Uma função send_data(payload: dict) -> dict que faça um POST pra https://httpbin.org/post enviando o payload como json,
# e retorne a resposta convertida. A httpbin devolve o que você mandou dentro da chave json da resposta, então você pode verificar que seus dados chegaram.
# Uma função get_with_params(params: dict) -> dict que faça um GET pra https://httpbin.org/get passando os params, 
# e retorne a resposta. A httpbin devolve os params recebidos na chave args.
# Uma função get_with_headers(headers: dict) -> dict que faça um GET pra https://httpbin.org/headers com headers customizados, 
# e retorne a resposta. Ela devolve os headers na chave headers.
# Trate erros com try/except em cada uma (a requisição pode falhar).
# No corpo principal, chame as três com dados de exemplo e imprima partes relevantes das respostas, mostrando que os dados, params e headers chegaram.
import requests

def send_data(payload: dict) -> dict:
    try:
        response = requests.post("https://httpbin.org/post", json=payload)
        if response.status_code != 200:
            return {"error": "Request Failed", "status": response.status_code}
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def get_with_params(params: dict) -> dict:
    try:
        response = requests.get("https://httpbin.org/get", params=params)
        if response.status_code != 200:
            return {"error": "Request Failed", "status": response.status_code}
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def get_with_headers(headers: dict) -> dict:
    try:
        response = requests.get("https://httpbin.org/headers", headers=headers)
        if response.status_code != 200:
            return {"error": "Request Failed", "status": response.status_code}
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

payload = {"name":"Lucas", "job":"Developer"}
print(send_data(payload))

params = {"page": 1, "per_page": 2}
print(get_with_params(params))

headers={"Accept": "application/json", "User-Agent": "meu-app"}
print(get_with_headers(headers))