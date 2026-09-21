# (review extra) delete com relacionamento e cascade
# Tema: o que acontece com os filhos ao deletar o pai (cascade)

# Enunciado (cascade delete)
# Crie day-043/review.py. Reescreve do zero um relacionamento um-para-muitos (pode ser o mesmo Author/Book, ou outro tema: 
# Playlist/Song, Category/Product). O programa deve:

# Os dois modelos relacionados, MAS com uma diferença no relationship do pai: configure o cascade. No lado do pai (o que tem a lista), adicione o cascade no relationship:
# python
# books: Mapped[list["Book"]] = relationship(
#     back_populates="author",
#     cascade="all, delete-orphan"
# )
# O cascade="all, delete-orphan" diz: quando o autor for deletado, delete os livros dele junto; e se um livro for removido da lista do autor, delete ele também (fica órfão).
# Crie um autor com 2 ou 3 livros ligados a ele.
# Uma função delete_author(author_id) que delete o autor. Por causa do cascade, os livros dele devem sumir junto.
# Demonstre no corpo principal:
# crie o autor com os livros
# liste todos os livros do banco (mostra que existem)
# delete o autor
# liste todos os livros de novo (os livros dele devem ter sumido também, por causa do cascade)
from sqlalchemy import Integer, String, select, create_engine, ForeignKey
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, sessionmaker, relationship

class Base(DeclarativeBase):
    pass

class Singer(Base):
    __tablename__="singers"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    songs: Mapped[list["Song"]] = relationship(
        back_populates="singer",
        cascade="all, delete-orphan"
    )

class Song(Base):
    __tablename__="songs"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    singer_id: Mapped[int] = mapped_column(Integer, ForeignKey("singers.id"))
    singer: Mapped["Singer"] = relationship(back_populates="songs")
    
    def __str__(self):
        return f"title: {self.title}, singer: {self.singer.name}"

engine = create_engine("sqlite:///playlists.db")
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

def create_singer(name: str) -> dict:
    verify_singer = db.execute(select(Singer).where(Singer.name == name)).scalars().first()
    if verify_singer:
        return {"message": "singer already existed in database"}
    
    new_singer = Singer(**{"name":name})
    
    db.add(new_singer)
    db.commit()
    return {
        "message": "singer added in database",
        "id": new_singer.id,
        "name": new_singer.name
    }

def create_song(data: dict) -> dict:
    verify_song = db.execute(select(Song).where(Song.title == data["title"])).scalars().first()
    if verify_song:
        return {"message": "song already existed in database"}
    
    new_song = Song(**data)
    db.add(new_song)
    db.commit()
    return {"message": "song created successfully"}

def get_singer(singer_id: int) -> dict:
    singer = db.execute(select(Singer).where(Singer.id == singer_id)).scalars().first()
    if not singer:
        return {"message": "singer not found"}
    
    return {
        "id": singer.id,
        "singer": singer.name,
        "songs": [song.title for song in singer.songs]
    }

def get_song(song_id: int) -> dict:
    song = db.execute(select(Song).where(Song.id == song_id)).scalars().first()
    if not song:
        return {"message": "song not found"}
    return {
        "song": song.title,
        "singer": song.singer.name
    }

def delete_singer(singer_id: int) -> dict:
    singer = db.execute(select(Singer).where(Singer.id == singer_id)).scalars().first()
    if not singer:
        return {"message": "singer not found"}
    
    db.delete(singer)
    db.commit()
    
    return {"message": "singer was deleted successfully"}

print(create_singer("Katy Perry"))

last_friday_night = {"title": "Last Friday Night (T.G.I.F)", "singer_id":1}
dark_horse = {"title": "Dark Horse", "singer_id":1}
et = {"title":"E.T.", "singer_id":1}

print(create_song(last_friday_night))
print(create_song(dark_horse))
print(create_song(et))

print(get_singer(1))
print(get_song(1))

print(delete_singer(1))

print(get_singer(1))
print(get_song(1))
print(get_song(2))
print(get_song(3))