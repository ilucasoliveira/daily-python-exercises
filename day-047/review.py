# (review extra) cadastro e login com senha hasheada no banco
# Tema: guardar usuário com senha hasheada no banco e verificar login

# Enunciado (user auth)
# Crie day-047/review.py. Junta bcrypt com SQLAlchemy (SQLite). O programa deve:

# Um modelo User (SQLAlchemy) com id, username (único) e hashed_password (repara no nome: você guarda o HASH, nunca a senha). Setup do banco (engine, session, create_all).
# As funções hash_password e verify_password (reaproveita a lógica de hoje, com bcrypt direto).
# Uma função register_user(username: str, password: str) -> dict que:
# verifique se o username já existe (retorna erro se sim)
# faça o hash da senha recebida
# crie o User com o username e o hash (NÃO a senha original), add, commit
# retorne sucesso
# Uma função login(username: str, password: str) -> dict que:
# busque o usuário pelo username (retorna erro se não existir)
# use verify_password pra comparar a senha digitada com o hash guardado
# retorne "login successful" se bater, "invalid credentials" se não
# No corpo principal, demonstre:
# registre um usuário
# tente registrar o mesmo username de novo (deve barrar)
# faça login com a senha CORRETA (deve funcionar)
# faça login com a senha ERRADA (deve falhar)
# tente login com um username que não existe (deve falhar)
import bcrypt
from sqlalchemy import Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__="users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(100))
    hashed_password: Mapped[str] = mapped_column(String(256))

engine = create_engine("sqlite:///users_hashed.db")
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()

def verify_password(plain: str, hashed: str) -> bool:
    return bcrypt.checkpw(plain.encode(), hashed.encode())

def register_user(username: str, password: str) -> dict:
    verify_user = db.execute(select(User).where(User.username == username)).scalars().first()
    if verify_user:
        return {"error": "username already existed in database"}
    
    hash_pwd = hash_password(password)
    new_user = User(username=username, hashed_password=hash_pwd)
    
    db.add(new_user)
    db.commit()
    return {"message": "user created successfully"}

def login(username: str, password: str) -> dict:
    user = db.execute(select(User).where(User.username == username)).scalars().first()
    if not user:
        return {"error": "invalid credentials"}
    
    verify_pwd = verify_password(password, user.hashed_password)
    if not verify_pwd:
        return {"error": "invalid credentials"}
    
    return {"message": "login successful"}

print(register_user("LionBr", "leaobrasileiro123"))
print(login("LionBr", "leaobrasileiro123"))

print(login("LionAmerican", "leaobrasileiro123"))
print(login("LionBr", "americanlion123"))
