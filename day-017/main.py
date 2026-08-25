# Enunciado do exercício (csv contacts)

# Crie day-017/main.py. Importe csv. O programa deve:

# Criar uma lista de pelo menos 3 contatos, cada um um dicionário com as colunas name, email e age
# Escrever esses contatos num arquivo .csv usando DictWriter, com cabeçalho (writeheader) e as linhas (writerows), lembrando do newline=""
# Ler o arquivo .csv de volta com DictReader e imprimir cada contato
# Ao ler, imprima também a soma ou a média das idades, lembrando de converter cada idade de texto para número com int()
# Usar with em todas as aberturas

import csv

users = [
    {"name":"Lucas","email":"lucas@gmail.com","age":23},
    {"name":"Isabella","email":"isabella@hotmail.com", "age":25},
    {"name":"Natanael","email":"natanael@yahoo.com", "age":19}
]

with open("users.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name","email","age"])
    writer.writeheader()
    writer.writerows(users)

with open("users.csv", "r") as file:
    reader = csv.DictReader(file)
    sum_age = 0
    for row in reader:
        print(row["name"], row["email"], row["age"])
        sum_age += int(row["age"])
    print(sum_age)