# Enunciado (blog api)
# Crie a pasta day-046 com main.py. Uma API FastAPI + SQLAlchemy (SQLite) de um mini blog, com relacionamento um-para-muitos entre autor e post. O programa deve:

# Dois modelos relacionados:
# Author (id, name) com relationship pros posts
# Post (id, title, content, author_id foreign key) com relationship pro autor
# foreign key no Post, relationship bidirecional (back_populates)
# Schemas Pydantic pra entrada: AuthorCreate (name) e PostCreate (title, content, author_id).
# Setup do banco (engine, get_db com yield, create_all) e o Depends(get_db) nas rotas.
# Rotas:
# POST /authors cria um autor (201)
# POST /posts cria um post ligado a um autor (valide que o autor existe, 404 se não; 201 se ok)
# GET /authors/{author_id} retorna o autor E a lista de posts dele, navegando pelo relationship (author.posts), não por consulta manual
# GET /posts/{post_id} retorna o post E o nome do autor dele (post.author.name)
# DELETE /authors/{author_id} deleta o autor (com cascade nos posts, o que você viu no review do day-043)
from pydantic import BaseModel, Field, field_validator

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import Integer, String, create_engine, select, ForeignKey
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import(
    DeclarativeBase,
    Mapped,
    mapped_column,
    sessionmaker,
    relationship,
    Session,
)

class Base(DeclarativeBase):
    pass

class Author(Base):
    __tablename__="authors"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(200), unique=True)
    posts: Mapped[list["Post"]] = relationship(
        back_populates="author",
        cascade="all, delete-orphan"
    )

class Post(Base):
    __tablename__="posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    content: Mapped[str] = mapped_column(String(1000))
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("authors.id"))
    author: Mapped["Author"] = relationship(back_populates="posts")

engine = create_engine("sqlite:///blog.db")
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class SchemaAuthor(BaseModel):
    name: str = Field(min_length=2, max_length=200)
    
    @field_validator("name")
    @classmethod
    def name_capitalize(cls, value):
        return value.capitalize()

class SchemaPost(BaseModel):
    title: str = Field(min_length=2, max_length=200)
    content: str = Field(min_length=5, max_length=1000)
    author_id: int = Field(ge=1)
    
    @field_validator("title")
    @classmethod
    def title_upper(cls, value):
        return value.title()

app = FastAPI(
    title="day-046: blog api",
    description="",
    version="1.0.0",
    contact={
        "name":"Lucas de Oliveira Pimentel",
        "email":"lucasoliveirapimentel.dev@gmail.com"
    }
)

@app.get("/")
def health_check():
    return {"status": "OK"}

@app.post("/authors", status_code=201)
def create_author(author: SchemaAuthor, db: Session = Depends(get_db)):
    verify_author = db.execute(select(Author).where(Author.name == author.name)).scalars().first()
    if verify_author:
        raise HTTPException(status_code=409, detail="author already created in database")
    
    new_author = Author(**author.model_dump())
    
    try:
        db.add(new_author)
        db.commit()
        db.refresh(new_author)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="author already created in database")
    
    return {
        "message": "author created successfully",
        "id": new_author.id,
        "name": new_author.name,
        "posts": []
    }

@app.post("/posts", status_code=201)
def create_post(post: SchemaPost, db: Session = Depends(get_db)):
    verify_post = db.execute(select(Post).where(Post.title == post.title)).scalars().first()
    if verify_post:
        raise HTTPException(status_code=409, detail="post already created in database")
    
    verify_author_created = db.execute(select(Author).where(Author.id == post.author_id)).scalars().first()
    if not verify_author_created:
        raise HTTPException(status_code=404, detail="author not found. Please, try again!")
    
    new_post = Post(**post.model_dump())
    
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return {
        "message": "post created successfully",
        "id": new_post.id,
        "title": new_post.title,
        "content": new_post.content,
        "author": new_post.author.name
    }

@app.get("/authors/{author_id}")
def get_author(author_id: int, db: Session = Depends(get_db)):
    author = db.execute(select(Author).where(Author.id == author_id)).scalars().first()
    if not author:
        raise HTTPException(status_code=404, detail="author not found")
    
    return {
        "id": author.id,
        "name": author.name,
        "posts": [{"id": p.id, "title": p.title} for p in author.posts]
    }

@app.get("/posts/{post_id}")
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.execute(select(Post).where(Post.id == post_id)).scalars().first()
    if not post:
        raise HTTPException(status_code=404, detail="post not found")
    
    return {
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "author": post.author.name
    }

@app.delete("/authors/{author_id}", status_code=204)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    author = db.execute(select(Author).where(Author.id == author_id)).scalars().first()
    if not author:
        raise HTTPException(status_code=404, detail="author not found")
    
    db.delete(author)
    db.commit()