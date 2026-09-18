# (review extra) salvar dados de API no banco
# Tema: consumir uma API pública e persistir os resultados com SQLAlchemy

# Enunciado (github users to database)
# Crie day-041/review.py. O programa deve buscar usuários do GitHub (a API do day-036/40, sem chave) e salvar no banco. 
# Reescreve do zero, não importa dos outros dias.

# Um modelo GithubUser (herdando de Base) com colunas: id (primary_key), username (String), name (String), public_repos (Integer). Adiciona um __str__.
# Setup do banco: engine SQLite (um arquivo tipo github_users.db), create_all, session.
# Uma função fetch_github_user(username: str) -> dict que consulte a API do GitHub e retorne os dados (username, name, public_repos), 
# com tratamento de erro (RequestException, status != 200). Retorno sempre dict.
# Uma função save_user(data: dict) -> None que receba os dados e crie um GithubUser no banco (add, commit). Só salva se os dados 
# não forem erro (o filtro do day-040, if "error" not in data).
# No corpo principal:
# busque 2 ou 3 usuários reais do GitHub (exemplo: "torvalds", "gvanrossum", o seu)
# salve cada um no banco
# depois consulte todos os usuários do banco e imprima
# faça também uma consulta com filtro (exemplo: usuários com mais de X repositórios)

# O ponto do dia: o fluxo completo API para banco. Você pega dados de fora (API externa), e em vez de só imprimir e perder, 
# você PERSISTE no banco. Da próxima vez, os dados estão lá, salvos. É o que um sistema real faz: consome, guarda, consulta.

import requests
from sqlalchemy import Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

class Base(DeclarativeBase):
    pass

class GithubUser(Base):
    __tablename__="githubusers"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(100))
    name: Mapped[str | None] = mapped_column(String(100))
    public_repos: Mapped[int] = mapped_column(Integer)
    
    def __str__(self):
        return f"ID {self.id}: {self.username} ({self.public_repos} repos)"

engine = create_engine("sqlite:///github_users.db")
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

def fetch_github_user(username: str) -> dict:
    try: 
        response = requests.get(f"https://api.github.com/users/{username}")
        if response.status_code != 200:
            return {"error": "username not found or invalid"}
        
        data = response.json()
        return {
            "username": data["login"],
            "name": data["name"],
            "public_repos": data["public_repos"]
        }
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def save_user(data: dict) -> None:
    if "error" not in data:
        new_user = GithubUser(**data)
        
        db.add(new_user)
        db.commit()

user1 = fetch_github_user("ilucasoliveira")
user2 = fetch_github_user("lucascanton")
user3 = fetch_github_user("ottaviorr")
save_user(user1)
save_user(user2)
save_user(user3)

users = db.execute(select(GithubUser)).scalars().all()
for user in users:
    print(user)

active = db.execute(
    select(GithubUser).where(GithubUser.public_repos > 10)
).scalars().all()
print("--- Users with more than 10 repos ---")
for user in active:
    print(user)