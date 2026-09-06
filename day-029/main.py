# Enunciado do exercício (custom context manager)

# Crie day-029/main.py. Importe contextmanager de contextlib. O programa deve:

# Um context manager timer_block que meça o tempo de execução do bloco: antes do yield marca o tempo de início, 
# depois do yield calcula e imprime a duração. Use com um bloco que faça algo (pode usar time.sleep pra simular demora).
# Um context manager tag que receba um nome de tag e imprima <nome> antes do bloco e </nome> depois 
# (simulando abertura e fechamento de uma tag HTML). Exemplo de uso: with tag("div"): imprime <div>, o conteúdo, e </div>.
# Um context manager safe_block que use try/finally em volta do yield: no try deixa o bloco rodar, 
# no finally imprime "Bloco finalizado" (provando que a limpeza roda mesmo se der erro dentro do bloco).
# No corpo principal, use os três com with, mostrando o comportamento de setup e cleanup de cada um.

from contextlib import contextmanager
import time

@contextmanager
def time_block():
    print("starting...")
    start = time.perf_counter()
    yield "file"
    print("finishing...")
    end = time.perf_counter()
    print (round(end - start, 2))

@contextmanager
def tag(name):
    print(f"starting {name}...")
    yield "content"
    print(f"finishing {name}...")

@contextmanager
def safe_block():
    try:
        yield "content"
    finally:
        print("section finished!")

with time_block():
    time.sleep(3)
    print(f"doing something")

with tag("HTML") as content:
    print(content)

with safe_block() as content:
    print("before ERROR")
    result = 10 / 0
    print("That's not run")