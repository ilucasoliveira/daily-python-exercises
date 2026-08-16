# Enunciado do exercício (list transformations)

# Crie day-008/main.py. Usando comprehensions (sem for solto com append), o programa deve:

# Partir de uma lista de números (exemplo: 1 a 10)
# Criar uma lista com o quadrado de cada número
# Criar uma lista só com os números pares da lista original (use if na comprehension)
# Partir de uma lista de palavras (exemplo: nomes) e criar uma lista com cada palavra em maiúsculas
# Criar uma lista só com as palavras que têm mais de 4 letras (use if)
# Imprimir cada resultado com um rótulo claro

numbers = [1,2,3,4,5,6,7,8,9,10]

square_numbers = [i ** 2 for i in numbers]

even_numbers = [i for i in numbers if (i % 2) == 0]

names = ["lucas", "geraldo", "silvana", "laura", "isabella", "marquinhos", "isa", "ana", "ju"]

upper_names = [i.upper() for i in names]

four_plus_names = [i for i in names if len(i) > 4]

print(square_numbers)
print(even_numbers)
print(upper_names)
print(four_plus_names)