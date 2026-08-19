# Enunciado do exercício (scope explorer)

# Crie day-011/main.py. O programa deve demonstrar escopo, nesta ordem:

# Criar uma variável global (exemplo: um nome ou um número)
# Criar uma função que tenha uma variável local de mesmo nome, com valor diferente, e imprima a local
# No corpo principal, chamar a função e depois imprimir a global, mostrando que a global não mudou
# Criar uma segunda função que receba um número por parâmetro, some algo a ele e retorne o resultado com return (a forma correta, sem global)
# No corpo principal, chamar essa função e imprimir o retorno, mostrando que a variável original de fora continua intacta

global_name = "--> Lucas Oliveira -->"
global_number = 10

def local_var():
    global_name = "<-- Oliveira Lucas <--"
    print(global_name)

local_var()
print(global_name)

def local_sum_number_two(number):
    global_number = number + 2
    return global_number

print(local_sum_number_two(5))
print(global_number)