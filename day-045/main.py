# Enunciado do exercício (dockerized api with postgres)

# Crie a pasta day-045. Reaproveite a API do day-044 (a de tasks), com estas mudanças. Precisa de vários arquivos:

# Um main.py: a API do day-044, MAS lendo a string de conexão do Postgres de uma variável de ambiente (os.getenv("DATABASE_URL")), não hardcoded.
# Instale o driver: adicione psycopg[binary] nas dependências.
# Um requirements.txt com fastapi, uvicorn, sqlalchemy, psycopg[binary].
# Um Dockerfile pra API (reaproveite a estrutura do day-013: base Python, copia, instala, expõe porta, roda uvicorn).
# Um docker-compose.yml com dois serviços:
# db: postgres:18, com as variáveis de ambiente (POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB) e o volume pra persistir
# api: build do seu Dockerfile, depends_on db, e a DATABASE_URL apontando pro serviço db
# Um .env (protegido no gitignore) com as credenciais, e o compose lendo delas.
import os

from dotenv import load_dotenv
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

load_dotenv()

DATABASE = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE)

SessionLocal = sessionmaker(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI(
    title="day-045: dockerized api with postgres",
    version="1.0.0",
    contact={
        "name": "Lucas de Oliveira Pimentel",
        "email": "lucasoliveirapimentel.dev@gmail.com"
    }
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

Base.metadata.create_all(engine)

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