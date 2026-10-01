# Enunciado do exercício (celery + fastapi)

# Crie a pasta day-054. Você vai precisar de dois arquivos principais:
# Um tasks.py com a app Celery configurada no Redis e uma tarefa demorada, tipo slow_add(x, y) que use time.sleep(5) e depois some (simula processamento pesado).
# Reaproveita o que você sabe do day-53.

import time
from celery import Celery

celery_app = Celery(
    "tasks", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0"
)


@celery_app.task
def slow_add(x: int, y: int) -> dict:
    time.sleep(15)
    return {"result": x + y}
