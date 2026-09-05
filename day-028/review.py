# (review extra) gerador e decorador lado a lado
# Enunciado (side by side)
# Crie day-028/review.py. O programa deve ter os dois, trabalhando no mesmo tema (processar uma sequência de nomes), pra você ver a diferença:

# Parte 1, o gerador:
# Uma função geradora name_stream(names) que receba uma lista de nomes e produza com yield cada nome em maiúsculas, um por vez.

# Parte 2, o decorador:
# Um decorador count_calls que conte quantas vezes a função decorada foi chamada. Dica: você vai precisar de uma variável
# que sobrevive entre as chamadas. Uma forma simples é usar um atributo na própria 
# wrapper: começa wrapper.count = 0 fora do wrapper (logo antes do return wrapper), e dentro do wrapper faz wrapper.count += 1 e imprime o valor a cada chamada.
# Uma função greet(name) decorada com @count_calls que retorne uma saudação pro nome.

# Parte 3, juntando:
# No corpo principal:
# percorra o name_stream com um for e, pra cada nome que ele produzir, chame o greet decorado
# assim você vê o gerador entregando nomes um por vez, e o decorador contando as chamadas do greet
# imprima o resultado de cada greet

def name_stream(names):
    for name in names:
        yield name.capitalize()

def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"calls: {wrapper.count}")
        result = func(*args, **kwargs)
        return result
    wrapper.count = 0
    return wrapper

@count_calls
def greet(name):
    return f"Hello {name}, Welcome!"

list_names = ["lucas", "silvana", "geraldo", "laura", "isabella", "gabriela", "daniela"]

for name in name_stream(list_names):
    print(greet(name))
