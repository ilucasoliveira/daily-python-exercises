# Enunciado do exercício (auth api)

# Crie a pasta day-049 com main.py. Uma API FastAPI de autenticação. Junta bcrypt, JWT, SQLAlchemy. 
# Instale: pip install fastapi uvicorn sqlalchemy pyjwt bcrypt python-dotenv "python-multipart". (o python-multipart é necessário pro form de login).

# O programa deve ter:
# O modelo User (id, username único, hashed_password), setup do banco, get_db.
# As funções de senha (hash/verify) e token (create/verify), reaproveitando o que você fez nos dias 47 e 48. SECRET_KEY do .env.
# Uma rota POST /register que recebe username e password (via um schema Pydantic), cria o usuário com senha hasheada, barra username duplicado (400 ou 409).
# Uma rota POST /login que recebe as credenciais e, se corretas, devolve o token JWT. Dica: use OAuth2PasswordRequestForm do FastAPI pra receber
# o login no formato padrão (username e password num form). Se as credenciais falharem, 401.
# A dependência get_current_user (como no exemplo) e uma rota protegida GET /me que retorna os dados do usuário logado, exigindo token válido.
import os
import jwt
import bcrypt

from pydantic import BaseModel, Field
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import Integer, String, create_engine, select
from sqlalchemy.orm import(
    DeclarativeBase,
    Mapped,
    mapped_column,
    sessionmaker,
    Session,
)

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
EXPIRE_TOKEN = int(os.getenv("EXPIRE_TOKEN", 30))

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(100), unique=True)
    hashed_password: Mapped[str] = mapped_column(String(256))

class SchemaUser(BaseModel):
    username: str = Field(min_length=2, max_length=100, description="type your username here")
    password: str = Field(min_length=5, max_length=255, description="type your password here")

engine = create_engine("sqlite:///users_hashed.db")
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()

def verify_password(plain: str, hashed: str) -> bool:
    return bcrypt.checkpw(plain.encode(), hashed.encode())

def create_token(username: str) -> str:
    exp = datetime.now(timezone.utc) + timedelta(minutes=EXPIRE_TOKEN)
    payload = {
        "sub": username,
        "exp": exp
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str) -> dict:
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.exceptions.ExpiredSignatureError as e:
        return {"error": str(e)}
    except jwt.exceptions.InvalidTokenError as i:
        return {"error": str(i)}
    
    return decoded

def raise_http_error(status_code: int, detail: str) -> None:
    raise HTTPException(status_code=status_code, detail=detail)

app = FastAPI(
    title="day-049: auth api",
    version="0.1.0",
    contact={
        "name":"Lucas de Oliveira Pimentel",
        "email":"lucasoliveirapimentel.dev@gmail.com"
    }
)

@app.get("/health", status_code=200, tags=["health"])
def health_check():
    return {"status": "OK"}

@app.post("/register", status_code=201)
def register_user(user: SchemaUser, db: Session = Depends(get_db)):
    verify_user = db.execute(select(User).where(User.username == user.username)).scalars().first()
    if verify_user:
        raise_http_error(409, "username already created in database. Please, try another username!")
    
    hashed = hash_password(user.password)
    new_user = User(username=user.username, hashed_password=hashed)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {
        "id": new_user.id,
        "username": new_user.username,
        "message": "user created successfully"
    }

@app.post("/login", status_code=200)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.execute(select(User).where(User.username == form_data.username)).scalars().first()
    if not user:
        raise_http_error(401, "unauthorized credentials")
    
    verify_pwd = verify_password(form_data.password, user.hashed_password)
    if not verify_pwd:
        raise_http_error(401, "unauthorized credentials")
    
    token = create_token(form_data.username)
    return {"access_token": token, "token_type": "bearer"}

oauth_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth_scheme), db: Session = Depends(get_db)):
    payload = verify_token(token)
    if "error" in payload:
        raise_http_error(401, "invalid or expired token")
    
    username = payload["sub"]
    
    user = db.execute(select(User).where(User.username == username)).scalars().first()
    if not user:
        raise_http_error(401, "user not found")
    
    return user

@app.get("/me", status_code=200)
def read_me(current_user: User = Depends(get_current_user)):
    return {"username": current_user.username}