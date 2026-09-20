# Enunciado do exercício (relationships)

# Crie a pasta day-043 com main.py. SQLAlchemy com SQLite. Monte um relacionamento um-para-muitos a seu critério 
# (Author/Book, Category/Product, User/Post, o que preferir). O programa deve:

# Dois modelos relacionados: o "pai" (ex: Author) e o "filho" (ex: Book), com a foreign key no filho e o relationship nos dois lados (back_populates).
# Criar o banco (create_all).
# Inserir pelo menos 1 pai e 2 ou 3 filhos ligados a ele. Dica: você pode criar os filhos e ligar via o relationship (autor.books.append(livro))
# ou setando o author no livro. As duas formas funcionam.
# Consultar o pai e imprimir os filhos dele navegando pelo relationship (for book in author.books).
# Consultar um filho e imprimir o pai dele (book.author.name), mostrando a navegação nos dois sentidos.
from sqlalchemy import Integer, String, ForeignKey, create_engine, select
from sqlalchemy.orm import(
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
    sessionmaker,
    )

class Base(DeclarativeBase):
    pass

class Author(Base):
    __tablename__ = "authors"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(150), unique=True)
    books: Mapped[list["Book"]] = relationship(back_populates="author")

class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(150))
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("authors.id"))
    author: Mapped["Author"] = relationship(back_populates="books")
    
    def __str__(self):
        return f"Book {self.id}: {self.title}"

engine = create_engine("sqlite:///library.db")
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

def create_author(name: str) -> dict:
    verify_author = db.execute(select(Author).where(Author.name == name)).scalars().first()
    if verify_author:
        return {"message": "author already existed in database"}
    
    new_author = Author(**{"name":name})
    
    db.add(new_author)
    db.commit()
    return {"message": "author added in database"}

def create_book(data: dict) -> dict:
    verify_book = db.execute(select(Book).where(Book.title == data["title"])).scalars().first()
    if verify_book:
        return {"message": "book already existed in database"}
    
    new_book = Book(**data)
    db.add(new_book)
    db.commit()
    return {"message": "book created successfully"}

def get_author(author_id: int) -> dict:
    author = db.execute(select(Author).where(Author.id == author_id)).scalars().first()
    if not author:
        return {"message": "author not found"}
    
    return {
        "id": author.id,
        "author": author.name,
        "books": [book.title for book in author.books]
    }

def get_book(book_id: int) -> dict:
    book = db.execute(select(Book).where(Book.id == book_id)).scalars().first()
    if not book:
        return {"message": "book not found"}
    return {
        "book": book.title,
        "author": book.author.name
    }

book1 = {
    "title":"The Lord of The Rings: The Fellowship of the Ring",
    "author_id":1
    }

book2= {
    "title": "The Hobbit",
    "author_id":1
}

print(create_author("J.R.R Tolkien"))
print(create_book(book1))
print(create_book(book2))
print(get_author(1))
print(get_book(1))
print(get_book(2))