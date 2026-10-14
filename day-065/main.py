# Exercício 1: day-065/main.py
# Uma rota POST /orders que recebe um pedido e publica no topic "orders".

# O que você precisa montar:
# Um modelo Pydantic Order com dois campos: item (str) e quantity (int). Lembra: anotação com :, não =
# O producer criado uma vez só, fora da rota, no topo do arquivo. Pergunta pra você responder: por que não criar ele dentro da rota?
# A mensagem agora é um dicionário, não texto. O Kafka só aceita bytes. O caminho é: dicionário vira texto JSON, texto vira bytes.
# Você já conhece as duas pontas: o módulo json tem uma função que transforma dict em string (dumps), e string vira bytes com .encode().
# O Pydantic te dá o dict com .model_dump()
# A rota responde na hora com algo tipo {"status": "order published"}
# Logging avisando que publicou
import logging

from fastapi import FastAPI
from pydantic import BaseModel, Field
from kafka import KafkaProducer

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.getLogger("kafka").setLevel(logging.WARNING)
logging.getLogger("watchfiles").setLevel(logging.WARNING)
logger = logging.getLogger()


producer = KafkaProducer(bootstrap_servers="localhost:9092")


class SchemaOrder(BaseModel):
    item: str = Field(min_length=2, max_length=100)
    quantity: int = Field(ge=1)


app = FastAPI()


@app.post("/orders", status_code=201)
def create_order(order: SchemaOrder):
    data = order.model_dump_json()
    producer.send("orders", data.encode())
    logger.info(f"item: {order.item} and quantity: {order.quantity} published")
    return {"status": "order published"}
