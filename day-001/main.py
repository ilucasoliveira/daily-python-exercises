# Enunciado do exercício (word inspector)

# Crie o arquivo day-001/main.py no repositório daily-exercises. O programa deve:

# Ler uma palavra do teclado com input()
# Imprimir, nesta ordem, uma por linha:
# a primeira letra
# a última letra (use índice negativo)
# a palavra invertida
# os 3 primeiros caracteres
# a palavra pulando de 2 em 2 caracteres
# Imprimir True ou False dizendo se a palavra é um palíndromo, usando apenas fatiamento e comparação, sem loop e sem if

# Critérios de pronto: as 6 saídas corretas para qualquer palavra digitada, e pelo menos 1 commit no GitHub.

def order_print():
    word = input("Digite uma palavra: ").strip()
    
    print(word[0])
    print(word[-1])
    print(word[::-1])
    print(word[0:3])
    print(word[::2])
    print(word[::-1] == word)

order_print()