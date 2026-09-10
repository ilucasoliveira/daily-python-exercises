# Enunciado do exercício (advanced tests)

# Crie a pasta day-033 com dois arquivos:

# Um functions.py com:
# uma função divide(a, b) que divida a por b (vai levantar ZeroDivisionError naturalmente se b for 0)
# uma função get_age(birth_year) que calcule a idade, mas levante um ValueError se o ano for no futuro (use raise ValueError("mensagem") pra levantar de propósito)
# uma função is_even(n) que retorne True se par, False se ímpar
# Um test_functions.py com:
# um teste usando pytest.raises pra verificar que divide levanta ZeroDivisionError ao dividir por zero
# um teste usando pytest.raises pra verificar que get_age levanta ValueError com ano futuro
# um teste parametrizado pro is_even com pelo menos 4 casos diferentes (incluindo o zero)
from datetime import datetime

def divide(a: int | float, b: int | float) -> float:
    return round(a / b, 2)

def get_age(birth_year: int) -> int:
    today = datetime.now().year
    if birth_year > today:
        raise ValueError("Birth year cannot be in the future")
    return today - birth_year

def is_even(n: int) -> bool:
    return n % 2 == 0
