# Enunciado do exercício (my first module)

# Crie a pasta day-020 com dois arquivos:

# Um arquivo operations.py (o módulo) contendo pelo menos 3 funções úteis, cada uma com return. 
# Exemplo: uma que soma uma lista de números, uma que acha o maior de uma lista, uma que conta quantos itens tem. Fica a seu critério o tema.
# Um arquivo main.py que importe o operations e use as 3 funções, imprimindo os resultados.

from operations import sum_number, the_biggest, even_numbers

numbers = [1,2,3,4,5,10,15,20,25,30,99,100,101,102,103]

print(sum_number(numbers))
print(the_biggest(numbers))
print(even_numbers(numbers))