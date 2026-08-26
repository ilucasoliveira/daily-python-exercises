# Enunciado do exercício (safe converter)

# Crie day-018/main.py. O programa deve ter:

# Uma função safe_divide(a, b) que tente dividir a por b e retorne o resultado, mas capture ZeroDivisionError e retorne uma mensagem amigável se b for zero
# Uma função safe_int(text) que tente converter um texto pra número inteiro e retorne o número, mas capture ValueError e retorne None (ou uma mensagem) se não der
# Uma função read_file_safe(filename) que tente abrir e ler um arquivo, mas capture FileNotFoundError e retorne uma mensagem amigável se o arquivo não existir
# No corpo principal, chame cada função duas vezes: uma com entrada que funciona e outra com entrada que causa o erro, mostrando que o programa não quebra em nenhum caso

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Divisor cannot be zero. Please, try again!"
    
    return result

def safe_int(text):
    try:
        value = int(text)
    except ValueError:
        return None
    
    return value

def read_file_safe(filename):
    try:
        with open(filename, "r") as file:
            content = file.read() 
    except FileNotFoundError:
        return "File Not Found. Please, Try again!"
    
    return content

print(safe_divide(10, 2))
print(safe_divide(15, 0))
print(safe_int("1971"))
print(safe_int("1971s"))
print(read_file_safe("products"))