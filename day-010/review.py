# Crie day-010/review.py. O programa deve ter:

# Uma função create_order(customer, *items, **details) que receba:
# customer: um argumento normal, o nome do cliente
# *items: qualquer quantidade de produtos (posicionais)
# **details: qualquer quantidade de detalhes nomeados (exemplo: payment="pix", discount=10)
# A função deve retornar (não imprimir) um dicionário com três chaves:
# "customer": o nome recebido
# "items": a lista de produtos (dica: items chega como tupla, você pode devolver como está ou converter pra lista)
# "details": o dicionário de detalhes
# No corpo principal, chamar create_order pelo menos duas vezes, com quantidades diferentes de items e details, e imprimir cada retorno

def create_order(customer, *items, **details):
    client = {
        "customer": customer,
        "items": list(items),
        "details": details
    }
    return client

print(create_order("Maria", "coffee", "milk", "cookie", payment="pix", discount=10))
print(create_order("Ana", "dress", "pants", "red lipstick",payment="credit card"))