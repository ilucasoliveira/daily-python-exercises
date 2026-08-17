# Enunciado do exercício (dict transformations)

# Crie day-009/main.py. Usando dict comprehensions, o programa deve:

# Partir de uma lista de palavras (exemplo: nomes) e criar um dicionário onde a chave é a palavra e o valor é o tamanho dela (use len)
# Partir de uma lista de números e criar um dicionário onde a chave é o número e o valor é o cubo dele (n ** 3)
# Criar um dicionário só com os pares do passo 1 cujo valor (tamanho) seja maior que 4 letras (use if na comprehension)
# Imprimir cada dicionário com um rótulo claro

# ------- names -------
list_names = ["lucas", "silvana", "geraldo", "laura", "isabella", "gabriela", "daniela", "duda", "ju", "kaka"]
dict_names = {i: len(i) for i in list_names}

# ------- numbers -------
list_numbers = [1,2,3,4,5,6,7,8,9,10]
dict_numbers = {i: i ** 3 for i in list_numbers}

# ------- big -------
big_names = {i: len(i) for i in list_names if len(i) > 4}

# ------- print -------
print(dict_names)
print(dict_numbers)
print(big_names)