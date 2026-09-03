# (review extra) pipeline de geradores

# Tema: encadear geradores pra processar dados por etapas

# O conceito que isso mostra: geradores podem ser encadeados. A saída de um vira a entrada de outro, formando um pipeline.
# Cada dado passa pelas etapas um de cada vez, sem nunca existir uma lista completa na memória. É assim que se processa arquivo gigante na vida real.

# Enunciado (number pipeline)

# Crie day-026/review.py. O programa deve:

# Uma função geradora generate_numbers(limit) que produza os números de 1 até limit com yield.
# Uma função geradora only_multiples(numbers, factor) que receba um gerador (ou qualquer iterável) de números e um fator, 
# e produza com yield só os números divisíveis por esse fator. Dica: percorre os numbers com for e dá yield só nos que passam no teste % factor == 0.
# Uma função geradora square_them(numbers) que receba números e produza o quadrado de cada um com yield.
# No corpo principal, encadeie os três formando um pipeline:
# gera números de 1 a 20
# passa pro only_multiples pra pegar só os múltiplos de 3
# passa pro square_them pra elevar ao quadrado
# percorre o resultado final com um for e imprime
# O encadeamento fica na linha do tipo: square_them(only_multiples(generate_numbers(20), 3))
# Imprima também a versão com list(...) do pipeline completo pra ver todos os resultados juntos.

def generate_numbers(limit):
    for n in range(1, limit + 1):
        yield n

def only_multiples(numbers, factor):
    for n in numbers:
        if n % factor == 0:
            yield n

def square_them(numbers):
    for n in numbers:
        yield n**2

def print_each(value):
    for i in value:
        print(i)

print_each(square_them(only_multiples(generate_numbers(20), 3)))

print_each(only_multiples(generate_numbers(10), 2))

print_each(generate_numbers(5))

print(list(square_them(only_multiples(generate_numbers(20), 3))))