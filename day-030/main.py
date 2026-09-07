# Enunciado do exercício (typed functions)

# Crie day-030/main.py. Escreva funções totalmente tipadas:

# Uma função add(a: int, b: int) -> int que some dois inteiros
# Uma função que receba uma list[float] e retorne a média como float
# Uma função que receba uma list[str] e retorne um dict[str, int] mapeando cada palavra ao seu tamanho
# Uma função que receba um int e retorne Optional[str] (ou str | None): retorna uma mensagem se o número for positivo, ou None se for negativo ou zero
# No corpo principal, chame todas e imprima os resultados

def add(a: int, b: int) -> int:
    return a + b

def average_list(float_list: list[float]) -> float:
    total = sum(float_list)
    quantity = len(float_list)
    return round(total / quantity, 2)

def list_to_dict(str_list: list[str]) -> dict[str, int]:
    result = {}
    for word in str_list:
        result[word] = len(word)
    return result

def int_to_str(x: int) -> str | None:
    if x > 0:
        return "positive number!"
    return None

list_float = [2.0, 3.59, 2.99, 2.5, 5.99, 10.80, 11.43, 12.0]
print(average_list(list_float))

list_str = ["lucas", "silvana", "geraldo", "isabella", "laura"]
print(list_to_dict(list_str))

print(int_to_str(10))
print(int_to_str(-1))