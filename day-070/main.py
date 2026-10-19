import os
import json
import logging
import uuid

from dotenv import load_dotenv
from fastapi import FastAPI
from kafka import KafkaProducer
from pydantic import BaseModel, Field

load_dotenv()  # Load environment variables from .env file

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.getLogger("kafka").setLevel(logging.WARNING)
logging.getLogger("watchfiles").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

app = FastAPI()

producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)


class SchemaOrder(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    quantity: int = Field(ge=1)


@app.post("/orders", status_code=201)
def create_order(order: SchemaOrder):
    order_id = str(uuid.uuid4())
    order_dict = order.model_dump()
    order_dict["order_id"] = order_id

    producer.send("orders", value=json.dumps(order_dict).encode("utf-8"))
    producer.flush()

    logger.info(
        f"Order published: {order_id}, name: {order.name}, quantity: {order.quantity}"
    )
    return {"order_id": order_id, "status": "published"}
