import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, Integer, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class ProcessedOrder(Base):
    __tablename__ = "processed_orders"
    order_id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str | None] = mapped_column(String(50))
    quantity: Mapped[int | None] = mapped_column(Integer)


load_dotenv()

DATABASE = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE)
SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(engine)
