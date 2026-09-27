# Enunciado (notes api)

# Crie a pasta day-050 com main.py. Uma API de notas onde cada nota pertence a um usuário. Reaproveite a base de autenticação
# do day-049 (User, hash, token, register, login, get_current_user). Adicione:

# Um modelo Note (id, title, content, owner_id foreign key pra User) com relationship. E no User, o relationship pros notes (com cascade, do day-43).
# Um schema Pydantic NoteCreate (title, content). Repara: o owner NÃO vem no schema, ele é o usuário logado, você pega do token.
# Rotas protegidas (todas exigem get_current_user):
# POST /notes cria uma nota ligada ao usuário logado (o owner_id vem do current_user, não do corpo)
# GET /notes lista só as notas do usuário logado (filtra por owner_id, não retorna as dos outros)
# GET /notes/{note_id} retorna uma nota, mas só se for do usuário logado (senão 403 ou 404)
# DELETE /notes/{note_id} deleta uma nota, mas só se for do usuário logado (se for de outro, 403)
import os
import jwt
import bcrypt

from dotenv import load_dotenv
from pydantic import BaseModel, Field, field_validator
from datetime import datetime, timezone, timedelta
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import(
    Integer,
    String,
    create_engine,
    select,
    ForeignKey,
)
from sqlalchemy.orm import(
    DeclarativeBase,
    Mapped,
    mapped_column,
    sessionmaker,
    Session,
    relationship,
)

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
EXPIRE_TOKEN = int(os.getenv("EXPIRE_TOKEN", 30))

class Base(DeclarativeBase):
    pass

class Note(Base):
    __tablename__ = "notes"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    content: Mapped[str] = mapped_column(String(1000))
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    owner: Mapped["User"] = relationship(back_populates="notes")

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(150), unique=True)
    hashed_password: Mapped[str] = mapped_column(String(256))
    notes: Mapped[list["Note"]] = relationship(
        back_populates="owner",
        cascade="all, delete-orphan"
    )

class SchemaUser(BaseModel):
    username: str = Field(min_length=2, max_length=100)
    password: str = Field(min_length=5, max_length=256)

class SchemaNote(BaseModel):
    title: str = Field(min_length=2, max_length=100)
    content: str = Field(min_length=2, max_length=1000)
    
    @field_validator("title")
    @classmethod
    def title_upper(cls, value):
        return value.title()

engine = create_engine("sqlite:///note_and_users.db")
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

def create_token_access(username: str) -> str:
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

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = verify_token(token)
    if "error" in payload:
        raise_http_error(401, "invalid or expired token")
    
    username = payload["sub"]
    user = db.execute(select(User).where(User.username == username)).scalars().first()
    if not user:
        raise_http_error(404, "user not found")
    
    return user

def raise_http_error(status_code: int, detail: str) -> None:
    raise HTTPException(status_code=status_code, detail=detail)

app = FastAPI(
    title="day-050: notes api",
    description="",
    version="0.1.0",
    contact={
        "name": "Lucas de Oliveira Pimentel",
        "email": "lucasoliveirapimentel.dev@gmail.com"
    }
)

@app.post("/register", status_code=201, tags=["user"])
def register_user(user: SchemaUser, db: Session = Depends(get_db)):
    verify_user = db.execute(select(User).where(User.username == user.username)).scalars().first()
    if verify_user:
        raise_http_error(409, "username already existed in database. Please try another one again!")
    
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

@app.post("/login", status_code=200, tags=["user"])
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.execute(select(User).where(User.username == form_data.username)).scalars().first()
    if not user:
        raise_http_error(401, "unauthorized credentials")
    
    verify_pwd = verify_password(form_data.password, user.hashed_password)
    if not verify_pwd:
        raise_http_error(401, "unauthorized credentials")
    
    token = create_token_access(form_data.username)
    return {"access_token": token, "token_type": "bearer"}

@app.get("/health", status_code=200, tags=["health"])
def health_check():
    return {"status": "OK"}

@app.post("/notes", status_code=201, tags=["notes"])
def create_note(notes: SchemaNote, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)) -> dict:
    verify_note = db.execute(select(Note).where(Note.owner_id == current_user.id, Note.title == notes.title)).scalars().first()
    if verify_note:
        raise_http_error(409, "note already created in your notes. Please try again!")
    
    owner_id = current_user.id
    new_note = Note(**notes.model_dump(), owner_id=owner_id)
    
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    
    return {
        "id": new_note.id,
        "owner": new_note.owner.username,
        "title": new_note.title,
        "content": new_note.content
    }

@app.get("/notes", status_code=200, tags=["notes"])
def read_notes(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    notes_user = db.execute(select(Note).where(Note.owner_id == current_user.id)).scalars().all()
    
    return [
        {"id": note.id, "title": note.title, "content": note.content}
        for note in notes_user
    ]

@app.get("/notes/{note_id}", status_code=200, tags=["notes"])
def read_note(note_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    note_user = db.execute(select(Note).where(Note.id == note_id)).scalars().first()
    
    if not note_user:
        raise_http_error(404, "note not found")
    
    if note_user.owner_id != current_user.id:
        raise_http_error(403, "you don't own this note")
    
    return {
        "id": note_user.id,
        "title": note_user.title,
        "content": note_user.content
    }

@app.delete("/notes/{note_id}", status_code=204, tags=["notes"])
def delete_note(note_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    note_user = db.execute(select(Note).where(Note.id == note_id)).scalars().first()
    
    if not note_user:
        raise_http_error(404, "note not found")
    
    if note_user.owner_id != current_user.id:
        raise_http_error(403, "you don't own this note")
    
    db.delete(note_user)
    db.commit()