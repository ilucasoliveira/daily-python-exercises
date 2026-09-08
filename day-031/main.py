# Enunciado do exercício (advanced typing)

# Crie day-031/main.py. Importe o que precisar de typing. O programa deve:

# Um type alias no topo, exemplo Number = int | float, e uma função que use ele: recebe dois Number e retorna um Number (soma que aceita int ou float)
# Uma função describe(value: int | str) -> str que receba int ou str e retorne uma descrição diferente conforme o
# tipo (dica: isinstance(value, int) testa se é int). Isso mostra o Union na prática.
# Um type alias pra uma estrutura de dados, exemplo Inventory = dict[str, int] (produto pra quantidade),
# e uma função que receba um Inventory e retorne o total de itens (soma dos valores)
# Uma função apply_operation(func: Callable[[int, int], int], a: int, b: int) -> int que receba uma função de dois inteiros
# e aplique nos dois números. Teste passando funções diferentes (uma que soma, uma que multiplica)
# No corpo principal, chame todas e imprima os resultados

from typing import Callable

Number = int | float
Inventory = dict[str, int]

def sum_numbers(num1: Number, num2: Number) -> Number:
    return num1 + num2

def describe(value: int | str) -> str:
    if isinstance(value, int):
        return f"value is instance int: {value}"
    return f"value is instance str: {value}"

def total_items(inventory: Inventory) -> int:
    counter = 0
    for value in inventory.values():
        counter += value
    return counter

def apply_operation(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

def apply_sum(a: int, b: int) -> int:
    return a + b

def apply_multiple(a: int, b: int) -> int:
    return a * b

print(sum_numbers(4, 4.59))
print(sum_numbers(6.69, 10))

print(describe(1987))
print(describe("I'm lucas, welcome!"))

dict_inventory = {
    "apple": 3,
    "graps": 45,
    "passionfruit": 32,
    "coconut": 13
}

print(total_items(dict_inventory))

print(apply_operation(apply_sum, 23, 17))
print(apply_operation(apply_multiple, 7, 6))

