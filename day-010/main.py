# Enunciado do exercício (flexible functions)

# Crie day-010/main.py. O programa deve ter:

# Uma função sum_all(*args) que receba qualquer quantidade de números e retorne a soma de todos (use return, não print)
# Uma função build_profile(**kwargs) que receba qualquer quantidade de pares nomeados e retorne um dicionário com eles (ou monte a saída a partir deles)
# No corpo principal, chamar sum_all com quantidades diferentes de números (exemplo: uma vez com 3, outra com 5) e imprimir os resultados
# Chamar build_profile passando pares nomeados diferentes (exemplo: name, age, city) e imprimir o resultado

def sum_all(*args):
    return sum(args)

def build_profile(**kwargs):
    return kwargs

print(sum_all(6,9,15))
print(sum_all(1,2,3,4,5))

print(build_profile(name="Lucas", age=23, city="Barbacena"))