# Enunciado do exercício (generators)

# Crie day-026/main.py. O programa deve ter:

# Uma função geradora count_up_to(limit) que use yield pra produzir os números de 1 até limit, um por vez. Percorra ela com um for e imprima os valores.
# Uma função geradora even_numbers(limit) que produza só os números pares de 0 até limit, usando yield. Percorra e imprima.
# Uma função geradora read_lines(text) que receba um texto com várias linhas (use \n pra separar) e produza uma linha por vez com yield. 
# Dica: você pode dar yield dentro de um for que percorre as linhas.
# No corpo principal, use as três, mostrando os valores que cada uma produz. Em pelo menos uma delas, imprima também o resultado de 
# list(gerador) pra ver todos os valores juntos.

def count_up_to(limit):
    for i in range(1, limit + 1):
        yield i

def even_numbers(limit):
    for i in range(limit + 1):
        if i % 2 == 0:
            yield i

def read_lines(text):
    for line in text.split("\n"):
        yield line

for n in even_numbers(10):
    print(n)

for n in count_up_to(10):
    print(n)

text = "lucas\nsilvana\ngeraldo\nlaura\nisabella\nnatanael"

for t in read_lines(text):
    print(t)

print(list(even_numbers(10)))