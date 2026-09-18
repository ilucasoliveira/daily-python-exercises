# Enunciado do exercício (first orm)

# Crie a pasta day-041 com main.py. Instale: pip install sqlalchemy. O programa deve:

# Definir um modelo (classe herdando de Base) a seu critério: um Product com id, name e price, ou um Task com id, title e done,
# o que preferir. Pelo menos 3 colunas, incluindo o id como primary_key.
# Criar o engine com SQLite (um arquivo .db) e criar as tabelas com create_all.
# Criar a session.
# Inserir pelo menos 3 registros (crie os objetos, add, commit).
# Consultar todos os registros e imprimir cada um. (dica: pra imprimir bonito, um __str__ no modelo ajuda, seu day-025).
# Consultar com filtro: busque um registro específico com session.query(Model).filter(Model.coluna == valor).first() e imprima.

from sqlalchemy import create_engine, Integer, String, Boolean, select
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, sessionmaker

class Base(DeclarativeBase):
    pass

class Task(Base):
    __tablename__="tasks"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    status: Mapped[bool | None] = mapped_column(Boolean, default=False)
    
    def __str__(self):
        return f"Task {self.id}: {self.name} (done={self.status})"

engine = create_engine("sqlite:///my_database.db")

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

task1 = Task(name="go to the market")
task2 = Task(name="pick the children up at the school")
task3 = Task(name="just rest during afternoon", status=True)
db.add_all([task1, task2, task3])
db.commit()

tasks = db.execute(select(Task)).scalars().all()

for task in tasks:
    print(task)

found = db.execute(select(Task).where(Task.id == 2)).scalars().first()
print("Filtered:", found)
