# No expenses.py, crie estas funções, todas com return quando fizer sentido:

# add_expense(expenses, description, amount): recebe a lista de despesas, uma descrição e um valor.
# Cria um dicionário com description, amount e uma data de hoje formatada como texto ("dd/mm/aaaa" com strftime). 
# Adiciona esse dicionário à lista e retorna a lista.
# save_expenses(filename, expenses): salva a lista em JSON com indent=4, usando with.
# load_expenses(filename): tenta carregar o JSON. Protege com try/except: se o arquivo não existir 
# (FileNotFoundError), retorna uma lista vazia. Use with e return.
# total_spent(expenses): recebe a lista e retorna a soma de todos os amounts.

import json
from datetime import datetime

def add_expense(expenses: list, description: str, amount: float):
    expenses.append({
        "description": description,
        "amount": amount,
        "date": datetime.now().strftime("%d/%m/%Y")
    })
    return expenses

def save_expenses(filename, expenses):
    with open(filename, "w") as file:
        json.dump(expenses, file, indent=4)

def load_expenses(filename):
    
    try:
        with open(filename, "r") as file:
            content = json.load(file)
    except FileNotFoundError:
        return []
    
    return content

def total_spent(expenses):
    amounts = [amount["amount"] for amount in expenses]
    return round(sum(amounts), 2)