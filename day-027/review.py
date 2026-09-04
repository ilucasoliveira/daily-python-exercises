# (review extra) decorador que trata erros

# Tema: um decorador que envolve a função com try/except

# O conceito que isso mostra: até agora seus decoradores adicionavam logs e tempo. Mas um dos usos mais comuns de decorador 
# na vida real é tratamento de erro: em vez de escrever try/except dentro de toda função, você cria um decorador que faz isso 
# e aplica onde precisar. Menos repetição, o mesmo princípio DRY que você aplicou ontem.

# Enunciado (safe decorator)

# Crie day-027/review.py. O programa deve:

# Um decorador safe que envolva a função num try/except. Se a função rodar normal, retorna o resultado dela. Se ela levantar 
# qualquer exceção, o decorador captura, imprime uma mensagem tipo "Error: {e}" e retorna None em vez de deixar o programa quebrar. 
# O wrapper deve aceitar *args, **kwargs.
# Uma função divide(a, b) decorada com @safe que retorne a divisão de a por b. Chame ela duas vezes: uma com valores normais 
# (funciona) e uma dividindo por zero (o decorador captura o erro sem quebrar o programa).
# Uma função get_item(data, key) decorada com @safe que retorne data[key] de um dicionário. Chame com uma chave que existe 
# (funciona) e uma que não existe (o decorador captura o KeyError).
# No corpo principal, chame as funções nos dois cenários cada, e mostre que o programa roda até o fim mesmo com os erros, imprimindo os resultados.

def safe(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print(f"Error: {e}")
            return None
        return result
    return wrapper

@safe
def divide(a, b):
    return round(a / b, 2)

@safe
def get_item(data, key):
    return data[key]

user = {
    "name":"Silvana",
    "age":54
}

result = divide(10, 3)
print(result)
result_error = divide(10, 0)
print(result_error)

user_result = get_item(user, "name")
print(user_result)
wrong_user = get_item(user, "email")
print(wrong_user)
