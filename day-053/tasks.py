# Enunciado do exercício (first celery task)

# Crie a pasta day-053. Com o Redis rodando, crie:
# Um tasks.py com a app Celery configurada (broker e backend no Redis) e pelo menos 2 tarefas com @app.task:
# uma add(x, y) que some (simples, pra ver funcionar)
# uma slow_task(n) que use time.sleep(n) pra simular trabalho demorado e retorne algo (isso simula a tarefa pesada que você não quer que trave o usuário)
# Um jeito de disparar as tarefas. Pode ser um run.py que importe as tarefas e use .delay(...), ou você dispara pelo terminal Python interativo.
import time
from celery import Celery

app = Celery(
    "tasks", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0"
)


@app.task
def sum_number(*args: int) -> int:
    return sum(args)


@app.task
def slow_task(n: int) -> str:
    time.sleep(n)
    return f"slept for {n} seconds"
