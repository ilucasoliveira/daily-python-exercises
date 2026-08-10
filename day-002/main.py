# Enunciado do exercício (shopping list manager)

# Começar com uma lista de compras já com 3 itens à sua escolha
# Imprimir a lista inicial e quantos itens ela tem (use len)
# Adicionar 2 novos itens no fim
# Remover 1 item específico pelo nome
# Trocar o primeiro item da lista por outro
# Imprimir a lista final e a nova quantidade de itens

shopping_list = ["T-shirt","Pants", "Shoes"]

print(f"Initial list: {shopping_list}")
print(f"Items: {len(shopping_list)}")

shopping_list.append("Dress")
shopping_list.append("Toys")

shopping_list.remove("Pants")

shopping_list[0] = "Clean Products"

print(f"Final list: {shopping_list}")
print(f"Items: {len(shopping_list)}")