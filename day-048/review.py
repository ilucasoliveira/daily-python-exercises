# (review extra) fluxo de login com token
# Tema: juntar hash + banco + JWT num fluxo de autenticação

# Enunciado (auth flow)
# Crie day-048/review.py. Junta bcrypt, SQLAlchemy e JWT. O programa deve:

# Um modelo User (id, username único, hashed_password) e o setup do banco. (reaproveita a estrutura do review de ontem)
# As funções de senha: hash_password e verify_password (bcrypt).
# As funções de token: create_token(username) e verify_token(token) (JWT, com SECRET_KEY do .env).
# Uma função register(username, password) que cria o usuário com a senha hasheada no banco (barra username duplicado).
# Uma função login(username, password) -> dict que:
# busca o usuário
# verifica a senha com verify_password
# se a senha bater, GERA e RETORNA um token (create_token)
# se não, retorna erro com mensagem genérica ("invalid credentials")
# Uma função get_current_user(token) -> dict que simula uma rota protegida:
# recebe o token
# valida com verify_token
# se válido, retorna quem é o usuário (o sub do payload)
# se inválido/expirado, retorna erro
# No corpo principal, demonstre o fluxo completo:
# registra um usuário
# faz login com senha correta, recebe um token
# usa esse token no get_current_user, deve identificar o usuário
# tenta login com senha errada, recebe erro (sem token)
# usa um token inválido no get_current_user, deve dar erro
import os
import jwt
import bcrypt

from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv
from sqlalchemy import Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM","HS256")
EXPIRE_TOKEN = int(os.getenv("EXPIRE_TOKEN", 30))

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(100), unique=True)
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

def create_token(username: str) -> str:
    exp = datetime.now(timezone.utc) + timedelta(minutes=EXPIRE_TOKEN)
    payload = {"sub": username, "exp": exp}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str) -> dict:
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError as e:
        return {"error": str(e)}
    except jwt.InvalidTokenError as i:
        return {"error": str(i)}
    
    return decoded

def register_name(username: str, password: str) -> dict:
    user = db.execute(select(User).where(User.username == username)).scalars().first()
    
    if user:
        return {"error": "username already existed in database"}
    
    hashed_pwd = hash_password(password)
    new_user = User(username=username, hashed_password=hashed_pwd)
    
    db.add(new_user)
    db.commit()
    
    return {
        "id": new_user.id,
        "username": new_user.username,
        "message": "user created successfully"
    }

def login(username: str, password: str) -> dict:
    user = db.execute(select(User).where(User.username == username)).scalars().first()
    if not user:
        return {"error": "invalid credentials"}
    
    verify_pwd = verify_password(password, user.hashed_password)
    if not verify_pwd:
        return {"error": "invalid credentials"}
    
    token = create_token(username)
    return {"your_token": token}

def get_current_user(token: str) -> dict:
    valid_token = verify_token(token)
    
    if "error" in valid_token:
        return {"error": valid_token["error"]}
    
    return {"username": valid_token["sub"]}

print(register_name("ilucasoliveira", "lionbr123"))

result_login = login("ilucasoliveira", "lionbr123")
print(result_login)

token = result_login["your_token"]
print(get_current_user(token))