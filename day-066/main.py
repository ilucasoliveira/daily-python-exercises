import uuid
import json
import logging

from pydantic import BaseModel, Field
from fastapi import FastAPI
from kafka import KafkaProducer

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.getLogger("kafka").setLevel(logging.WARNING)
logging.getLogger("watchfiles").setLevel(logging.WARNING)
logger = logging.getLogger()

producer = KafkaProducer(bootstrap_servers="localhost:9092")


class SchemaOrder(BaseModel):
    item: str = Field(min_length=2, max_length=50)
    quantity: int = Field(ge=1)


app = FastAPI()


@app.get("/health", tags=["health"])
def health_check():
    return {"status": "OK"}


@app.post("/orders", status_code=201)
def create_order(order: SchemaOrder):
    order_id = str(uuid.uuid4())

    new_order = order.model_dump()
    new_order["order_id"] = order_id
    data = json.dumps(new_order)

    producer.send("orders", data.encode())
    producer.flush()

    logger.info(
        f"order {new_order['order_id']}: item {order.item} with {order.quantity}x was published"
    )
    return {"order_id": new_order["order_id"], "status": "published"}
