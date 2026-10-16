import json
import logging
import uuid

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
    name: str = Field(min_length=2, max_length=50)
    quantity: int = Field(ge=1)


app = FastAPI()


@app.post("/orders", status_code=201)
def create_order(order: SchemaOrder):
    order_id = str(uuid.uuid4())
    dict_order = order.model_dump()
    dict_order["order_id"] = order_id

    data = json.dumps(dict_order)
    producer.send("orders", data.encode())
    producer.flush()

    logger.info(
        f"order {order_id}: {dict_order['quantity']}X {dict_order['name']} published"
    )

    return {"order_id": order_id, "status": "published"}
