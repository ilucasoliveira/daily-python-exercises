# Enunciado do exercício (refactor day-003)

# Crie a pasta day-007. Copie pra lá o main.py do day-003 como ponto de partida, e refatore:

# Crie uma função que receba um dicionário e imprima cada par no formato chave: valor (tire o for solto de dentro do corpo principal)
# Crie uma função que receba um dicionário e retorne quantas chaves ele tem
# No corpo principal, monte o dicionário do aluno e use suas funções para imprimir os pares e mostrar a contagem
# A saída final deve ser igual à do day-003, só a organização muda

def print_dic(dictionary):
    
    for key, value in dictionary.items():
        print(f"{key}:{value}")

def qtd_keys(dictionary):
    quantity = len(dictionary)
    return quantity

student = {"name":"Lucas", "age":23, "course":"Science Computer"}

print_dic(student)
print(qtd_keys(student))
