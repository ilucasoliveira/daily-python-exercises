# Enunciado do exercício (first decorators)

# Crie day-027/main.py. O programa deve:

# Um decorador log_call que, ao envolver uma função, imprima "Calling function..." antes de executá-la e 
# "Finished" depois. O wrapper deve aceitar *args, **kwargs e retornar o resultado da função original.
# Uma função decorada com @log_call que faça algo simples e retorne um valor (exemplo: somar dois números 
# e retornar a soma). Chame ela e imprima o retorno, mostrando que os prints do decorador aparecem em volta.
# Um segundo decorador timer que meça quanto tempo a função levou pra rodar, usando datetime (marca o tempo 
# antes, chama a função, marca depois, imprime a diferença). Aplique num função qualquer.
# No corpo principal, chame as funções decoradas e observe o comportamento adicionado.

import time
from datetime import datetime

def log_call(func):
    def wrapper(*args, **kwargs):
        print("Calling function...")
        result = func(*args, **kwargs)
        print("Finished")
        return result
    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime. now()
        print(end - start)
        return result
    return wrapper

@log_call
def sum_numbers(a,b):
    return a + b

result = sum_numbers(3,5)
print(result)

@timer
def building_dict(name, age, mother):
    time.sleep(3)
    return {
        "name": name,
        "age": age,
        "mother": mother
    }

result2 = building_dict(name="Lucas", age=23, mother="Silvana")
print(result2)
