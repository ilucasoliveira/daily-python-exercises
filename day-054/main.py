# Um main.py com a API FastAPI:
# uma rota POST /tasks que receba os dados, dispare a tarefa com .delay(), e retorne o task_id na hora (status "processing"), SEM esperar
# uma rota GET /tasks/{task_id} que consulte o estado da tarefa pelo id, retornando o status e, se já terminou, o resultado
from fastapi import FastAPI
from celery.result import AsyncResult
from tasks import slow_add, celery_app

app = FastAPI(
    title="day-054: celery + fastapi",
    version="0.1.0",
    contact={
        "name": "Lucas de Oliveira Pimentel",
        "email": "lucasoliveirapimentel.dev@gmail.com",
    },
)


@app.post("/tasks", status_code=201)
def start_task(x: int, y: int) -> dict:
    task = slow_add.delay(x, y)
    return {"task_id": task.id, "status": "processing"}


@app.get("/tasks/{task_id}", status_code=200)
def status_task(task_id: str) -> dict:
    result = AsyncResult(task_id, app=celery_app)
    return {
        "status": result.status,
        "result": result.result if result.ready() else None,
    }
