# Enunciado (task with retry)

# Crie day-053/review.py (as tarefas) e um jeito de disparar. Com o Redis rodando. O programa deve:
# Uma app Celery configurada no Redis (reaproveita do main).
# Uma tarefa unstable_task(self, n) que simule uma operação instável:
# marca com @app.task(bind=True, max_retries=3) (o bind=True dá acesso ao self da tarefa, e max_retries=3 permite até 3 tentativas)
# por dentro, simule uma falha aleatória: use random.random() e, se der abaixo de um valor (tipo 0.7), levante uma exceção
# se falhar, chame self.retry(countdown=2) pra tentar de novo em 2 segundos
# se passar, retorne sucesso
# Uma tarefa process_data(data) normal que receba uma lista e retorne alguma estatística (soma, média), simulando processamento.
# Um jeito de disparar as duas e ver o resultado.
import random
from celery import Celery

app = Celery(
    "tasks", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0"
)


@app.task(bind=True, max_retries=3)
def unstable_task(self, n: int) -> str:
    x = random.random()
    if x < 0.7:
        print(f"failed (x={x:.2f}), retrying...")
        raise self.retry(countdown=2)
    print(f"succeeded (x={x:.2f})")
    return f"success with {n}"


@app.task
def process_data(data: list) -> dict:
    total = sum(data)
    average = round(total / len(data), 2)
    return {"sum": total, "average": average}
