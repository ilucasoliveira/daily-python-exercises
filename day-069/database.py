import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, Integer, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class ProcessedOrder(Base):
    __tablename__ = "processed_order"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    order_id: Mapped[str] = mapped_column(String, unique=True, nullable=False)


class Stock(Base):
    __tablename__ = "stock"

    name: Mapped[str] = mapped_column(String(50), primary_key=True)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
