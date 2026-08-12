# Enunciado do exercício (unique tags)

# Crie day-004/main.py. O programa deve, nesta ordem:

# Começar com uma lista que tenha itens repetidos (exemplo: tags de um post)
# Imprimir a lista original e quantos itens ela tem
# Transformar essa lista em set para remover as duplicatas
# Imprimir o set resultante e quantos itens únicos sobraram
# Criar um segundo set com alguns itens em comum e outros diferentes
# Imprimir a interseção (o que está nos dois) e a união (tudo junto) dos dois sets

repeat_tags = ["python", "backend", "API", "python", "Docker", "API", "API", "FastAPI", "backend"]

print(f"list: {repeat_tags} \nitems: {len(repeat_tags)}")

unrepeat_tags = set(repeat_tags)

print(f"list: {unrepeat_tags} \nitems: {len(unrepeat_tags)}")

extra_tags = set(["backend", "Django", "frontend", "API"])

print(unrepeat_tags & extra_tags) # &: faz a interseção; o que está nos dois
print(unrepeat_tags | extra_tags) # |: faz a união; tudo junto sem repetir