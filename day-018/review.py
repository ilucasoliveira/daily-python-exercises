# Crie day-018/review.py. Importe json. O programa deve:

# Uma função save_json(filename, data) que salve um dicionário ou lista em JSON com indent=4. 
# Protege a escrita com try/except capturando um erro genérico de escrita não é o foco aqui, então pode manter simples, só o with e o dump. Use with.
# Uma função load_json(filename) que tente abrir e carregar o JSON, mas capture DOIS erros diferentes, cada um no seu except:
# FileNotFoundError: se o arquivo não existe, retorne uma mensagem amigável ou uma lista vazia
# json.JSONDecodeError: se o arquivo existe mas está com JSON inválido (corrompido), retorne outra mensagem amigável
# No corpo principal, teste os três cenários da load_json, mostrando que nenhum quebra o programa:
# carregar um arquivo válido que você acabou de salvar (funciona)
# carregar um arquivo que não existe, tipo "naoexiste.json" (cai no FileNotFoundError)
# carregar um arquivo corrompido (cai no JSONDecodeError)

import json

def save_json(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def load_json(filename):
    try:
        with open(filename, "r") as file:
            content = json.load(file)
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        return "The JSON file is corrupted. Please, try again!"
    
    return content

market_list = ["shampoo", "mousturizer cream", "conditioner", "soap", "cookies", "meat", "tomato sauce", "passion fruit", "rice and beans"]

print(load_json("marketproducts.json"))
save_json("marketproducts.json", market_list)
print(load_json("marketproducts.json"))

print(load_json("broken.json"))
