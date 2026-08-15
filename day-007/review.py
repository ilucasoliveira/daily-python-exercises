# Enunciado (contact processor)

# Crie day-007/review.py. O programa deve, nesta ordem:

# Começar com uma lista de nomes, alguns repetidos de propósito (exemplo: ["ana", "bruno", "ana", "carla", "bruno", "diego"])
# Criar uma função remove_duplicates(names) que receba a lista e retorne uma nova lista sem repetidos. Ela precisa retornar, não imprimir. Dica: você aprendeu no day-004 uma forma rápida de tirar duplicatas.
# Criar uma função get_every_second(names) que receba a lista e retorne apenas os nomes em posição par (índices 0, 2, 4...), usando fatiamento com passo. Precisa retornar, não imprimir. Cuidado com o número do passo, lembra do que travou você no day-001.
# Criar uma função replace_first(names, new_name) que receba a lista e um nome novo, substitua o primeiro item pelo novo (substituir, não inserir, lembra do day-002) e retorne a lista alterada.
# No corpo principal, chame as três funções na ordem e imprima cada resultado com um rótulo claro, sempre imprimindo fora da função, nunca dentro.

names_list = ["silvana", "laura", "geraldo", "lucas", "laura", "lohayne", "lucas", "lorena", "matheus", "isabella", "silvana", "gabriela", "daniela", "isabella", "laura"]

def remove_duplicates(names):
    value = set(names)
    return value

def get_every_second(names):
    even_names = names[::2]
    return even_names

def replace_first(names, new_name):
    new_list = names[:] # [:] serve para copiar a lista não apenas coloca-lá dentro de uma variável, alterando a real; .copy() tambem funciona;
    new_list[0] = new_name.lower()
    return new_list

print(remove_duplicates(names_list))
print(get_every_second(names_list))
print(replace_first(names_list, "Maria Joaquina"))