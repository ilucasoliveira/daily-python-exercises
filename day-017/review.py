# DIA 17 (review extra) converter CSV para JSON

# Tema: ler de um formato, escrever em outro, com funções separadas

# Enunciado (csv to json converter)

# Crie day-017/review.py. Importe csv e json. O programa deve:

# Uma função create_csv(filename, products) que receba um nome de arquivo e uma lista de produtos
# (cada um um dicionário com name, price e stock) e escreva no CSV com DictWriter, cabeçalho e linhas. Lembra do newline="". Use with.
# Uma função csv_to_json(csv_file, json_file) que:
# abra o CSV com DictReader
# monte uma lista com todas as linhas lidas (cada linha é um dicionário)
# salve essa lista num arquivo JSON com json.dump e indent=4
# use with nas duas aberturas
# No corpo principal: crie uma lista de pelo menos 3 produtos, gere o CSV com a primeira função,
# converta pra JSON com a segunda, e depois abra o JSON de volta pra imprimir e conferir que a conversão funcionou.

import csv
import json

def create_csv(filename, products):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "price", "stock"])
        writer.writeheader()
        writer.writerows(products)

def csv_to_json(csv_file, json_file):
    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)
        json_list = []
        for row in reader:
            row["price"] = float(row["price"])
            row["stock"] = int(row["stock"])
            json_list.append(row)
        with open(json_file, "w") as j_file:
            json.dump(json_list, j_file, indent=4)

products = [
    {"name":"Cereal", "price":3.14, "stock":110},
    {"name":"Hair Cream", "price":5.99, "stock":34},
    {"name":"Dogs Food to small breeds", "price":10.99, "stock":50}
]

create_csv("products.csv", products)
csv_to_json("products.csv", "products.json")

with open("products.json", "r") as file:
    data = json.load(file)
    print(data)