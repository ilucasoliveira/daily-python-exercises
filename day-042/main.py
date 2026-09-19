# Enunciado do exercício (crud operations)
# Crie a pasta day-042 com main.py. Use SQLAlchemy com SQLite. O programa deve ter cada operação numa função separada:

# Um modelo a seu critério (Task, Product, o que preferir) com pelo menos 3 colunas e um __str__.
# Uma função create_item(...) que receba os dados, crie o objeto, add e commit. (Create)
# Uma função list_items() que retorne todos os registros. (Read)
# Uma função get_item(item_id) que busque um registro por id e retorne. (Read específico)
# Uma função update_item(item_id, ...) que busque por id, mude um atributo e commite. Trate o caso do registro não existir. (Update)
# Uma função delete_item(item_id) que busque por id e delete. Trate o caso de não existir. (Delete)
# No corpo principal, demonstre o ciclo completo: crie alguns itens, liste, atualize um, delete outro, e liste de novo mostrando as mudanças.
from sqlalchemy import Integer, String, Float, select, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column
from pydantic import BaseModel, Field
class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__="products"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[float] = mapped_column(Float)
    description: Mapped[str | None] = mapped_column(String(300), default=None)
    
    def __str__(self):
        desc = self.description or "no content"
        return f"ID: {self.id}, product: {self.name}, price: {self.price}, description: {desc}"

class SchemaUpdate(BaseModel):
    name: str | None = Field(default=None, max_length=100)
    price: float | None = Field(default=None, ge=0)
    description: str | None = Field(default=None, max_length=300)

engine = create_engine("sqlite:///products.db")
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

def create_product(data: dict) -> None:
    verify_product = db.execute(select(Product).where(Product.name == data["name"])).scalars().first()
    
    if verify_product is None:
        new_product = Product(**data)
        db.add(new_product)
        db.commit()
        return {"message": "product created"}
    
    return {"message": "product already exists"}

def list_products() -> None:
    products = db.execute(select(Product)).scalars().all()
    if not products:
        return []
    for item in products:
        print(item)

def get_product(item_id: int) -> str:
    product = db.execute(select(Product).where(Product.id == item_id)).scalars().first()
    if not product:
        return "error: product not found!"
    print(product)

def update_item(item_id: int, update_data: SchemaUpdate) -> dict:
    product = db.execute(select(Product).where(Product.id == item_id)).scalars().first()
    if not product:
        return {"error": "product not found!"}
    
    new_data = update_data.model_dump(exclude_unset=True)
    
    for key, value in new_data.items():
        setattr(product, key, value)
    
    db.commit()
    return product

def delete_item(item_id: int) -> dict:
    product = db.execute(select(Product).where(Product.id == item_id)).scalars().first()
    if not product:
        return {"error": "product not found!"}
    
    db.delete(product)
    db.commit()
    return {"message": "product was deleted successfully"}

item1 = {"name":"teethbrush", "price": 3.15, "description": "A professional teethbrush for you!"}
item2 = {"name":"soda", "price": 3.99}
item3 = {"name":"rice", "price": 2.05}

create_product(item1)
create_product(item2)
create_product(item3)
list_products()
get_product(1)

update_item2 = SchemaUpdate(price=4.05, description="a delicious soda to drink whenever you want to!")
print(update_item(2, update_item2))
list_products()

print(delete_item(1))
list_products()