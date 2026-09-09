# Enunciado do exercício (first tests)
# Crie a pasta day-032 com dois arquivos:
# Um functions.py com pelo menos 3 funções simples pra testar (pode reaproveitar coisas suas: uma que soma, 
# uma que verifica se um número é par, uma que inverte uma string, o que preferir). Cada uma com return.
# Um test_functions.py que importe essas funções e tenha uma função de teste (começando com test_) pra cada uma, 
# com múltiplos assert cobrindo casos diferentes (normal, limite, etc.)

# Antes, instale o pytest:
# pip install pytest
# Critério de pronto: as 3 funções em um arquivo, os testes em outro, cada teste com vários asserts, 
# e o comando pytest rodando e passando todos. Mais pelo menos 1 commit.

# 4. Como testar
# De dentro de day-032:
# pytest
# O pytest acha sozinho os arquivos test_ e roda tudo. Você vê algo como "3 passed". Pra ver detalhes de cada teste, use pytest -v (verbose).
# Experimente também quebrar de propósito: mude um assert pra um valor errado (tipo assert add(2, 3) == 99) e rode de novo. 
# Veja como o pytest mostra o que esperava versus o que recebeu. Depois conserta.
# Confere você mesmo: quando um assert falha, o pytest te diz qual função e qual linha falhou? Isso é o valor do teste automatizado.

def sum_numbers(a: int, b: int) -> int:
    return a + b

def is_even_number(num: int) -> str:
    if num % 2 == 0:
        return "it is even"
    return "it is not even"

def upside_down(text: str) -> str:
    result = text[::-1]
    return result
