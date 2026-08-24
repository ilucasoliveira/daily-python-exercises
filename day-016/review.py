# Enunciado (users json database)

# Crie day-016/review.py. Importe json. O programa deve:

# Uma função save_users(filename, users) que receba um nome de arquivo 
# e uma lista de usuários (cada usuário é um dicionário com name e age) e salve tudo em JSON com indent=4. Use with.
# Uma função load_users(filename) que abra o arquivo JSON e retorne a lista de usuários carregada. Use with e return.
# Uma função filter_adults(users) que receba a lista de usuários e retorne só os que têm idade maior ou igual a 18. 
# Dica: você pode usar uma list comprehension com if, como no day-008.
# No corpo principal: crie uma lista com pelo menos 3 usuários (alguns com 18 ou mais, outros com menos), 
# salve no arquivo, carregue de volta, filtre só os adultos a partir do que foi carregado, e imprima os adultos.

import json

def save_users(filename, users):
    
    with open(filename, "w") as file:
        json.dump(users, file, indent=4)

def load_users(filename):
    
    with open(filename, "r") as file:
        data = json.load(file)
    
    return data

def filter_adults(users):
    result= [user for user in users if user["age"] >= 18]
    return result

users = [
    {"name":"Lucas", "age":18},
    {"name":"Ana Clara", "age":14},
    {"name":"Isabella", "age":25},
    {"name":"Maria Laura", "age":14}
]

save_users("users.json", users)

all_users = load_users("users.json")
print(all_users)

adults = filter_adults(all_users)
print(adults)