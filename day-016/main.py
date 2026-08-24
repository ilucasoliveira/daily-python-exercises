# Enunciado do exercício (json data store)

# Crie day-016/main.py. Importe json no topo. O programa deve:

# Criar um dicionário com dados de um usuário, com pelo menos: um nome (texto), uma idade (número) e uma lista de habilidades (lista de textos)
# Salvar esse dicionário num arquivo .json usando json.dump com indent=4
# Abrir o arquivo .json de volta e carregar com json.load numa variável
# Imprimir um valor específico do dado carregado (exemplo: só o nome, ou a lista de skills)
# Imprimir também o tipo da idade carregada com type(...), pra provar que voltou como número e não como texto
# Usar with em todas as aberturas

import json

user = {
    "name":"Lucas de Oliveira",
    "age":23,
    "skills": ["python", "redis", "fastapi", "sqlalchemy", "html", "css", "javascript", "docker", "git", "poetry"]
}

with open("user.json", "w") as file:
    json.dump(user, file, indent=4)
# .dump: o método que escreve um objeto Python como JSON num arquivo
# indent=4: formata com 4 espaços de recuo, deixando o arquivo legível

with open("user.json", "r") as file:
    data = json.load(file) # load: carregar o arquivo (ler)
    print(data["name"])
    print(type(data["age"]))

# Revisão rápida: json.dump grava objeto em arquivo, json.load lê de volta; 
# a versão com "s" (dumps/loads) é pra texto sem arquivo; e o JSON preserva 
# os tipos, número volta número, lista volta lista, sem conversão na mão.