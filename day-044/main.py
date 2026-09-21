# . Enunciado do exercício (api with database)

# Crie a pasta day-044 com main.py. Uma API FastAPI com banco SQLite via SQLAlchemy. Instale: pip install fastapi uvicorn sqlalchemy. O programa deve ter:

# Um modelo SQLAlchemy (ex: Task com id, title, done) e um modelo Pydantic pra validar a entrada (ex: TaskCreate com title).
# O setup do banco (engine, SessionLocal, create_all) e a função get_db com yield.
# Rotas que usam o banco via Depends(get_db):
# POST /tasks que recebe um TaskCreate, cria a task no banco, retorna ela (status 201)
# GET /tasks que lista todas as tasks do banco
# GET /tasks/{task_id} que retorna uma task por id (404 se não existir)
# DELETE /tasks/{task_id} que deleta uma task (404 se não existir)

# Critério de pronto: a API roda, as rotas leem e escrevem no banco de verdade (os dados persistem entre requisições e execuções),
# o Depends(get_db) injetando a session, e a validação Pydantic na entrada. Mais pelo menos 1 commit. E o *.db no gitignore.
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import Integer, String, Boolean, select, create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import(
    DeclarativeBase,
    Mapped,
    mapped_column,
    sessionmaker,
    Session,
)

class Base(DeclarativeBase):
    pass

class Task(Base):
    __tablename__="tasks"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), unique=True)
    done: Mapped[bool] = mapped_column(Boolean, default=False)

class SchemaTask(BaseModel):
    title: str = Field(min_length=2, max_length=100)
    done: bool | None = Field(default=False)

engine = create_engine("sqlite:///schedule_tasks.db")
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI(
    title="day-044: api with database",
    version="1.0.0",
    contact={
        "name":"Lucas de Oliveira",
        "email":"lucasoliveirapimentel.dev@gmail.com"
    }
)

@app.get("/")
def health_check():
    return {"status": "OK"}

@app.post("/tasks", status_code=201)
def create_task(task: SchemaTask, db: Session = Depends(get_db)):
    verify_task = db.execute(select(Task).where(Task.title == task.title)).scalars().first()
    if verify_task:
        raise HTTPException(status_code=409, detail="task already created in database")
    
    new_task = Task(**task.model_dump())
    
    try:
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="task already created in database")
    
    return {"id": new_task.id, "title": new_task.title, "done": new_task.done}

@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)) -> list:
    tasks = db.execute(select(Task)).scalars().all()
    if not tasks:
        return []
    
    result = []
    for task in tasks:
        result.append({
            "id": task.id,
            "title": task.title,
            "done": task.done
            })
    return result

@app.get("/tasks/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.execute(select(Task).where(Task.id == task_id)).scalars().first()
    if not task:
        raise HTTPException(status_code=404, detail="task not found")
    
    return {
        "id": task.id,
        "title": task.title,
        "done": task.done
    }

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.execute(select(Task).where(Task.id == task_id)).scalars().first()
    if not task:
        raise HTTPException(status_code=404, detail="task not found")
    
    db.delete(task)
    db.commit()