# Por que kafka:19092 aqui e localhost:9092 no FastAPI?
# O Kafka é um só, com duas portas de entrada. Cada programa usa a que alcança de onde roda:
# - O FastAPI roda no Windows: ele não conhece o nome "kafka" (só existe na rede do Docker),
#   então entra pela porta publicada em "ports", localhost:9092.
# - Este consumer roda num container: aqui "localhost" é o próprio container (sem Kafka),
#   mas ele está na rede do Docker, então entra por kafka:19092.
# Duas portas são necessárias porque o Kafka devolve ao cliente o endereço "anunciado"
# (KAFKA_ADVERTISED_LISTENERS) da porta por onde ele entrou, e cada lado precisa de um
# endereço que funcione de onde está.

import os
import json
import logging

from dotenv import load_dotenv
from kafka import KafkaConsumer
from sqlalchemy.exc import IntegrityError

from database import SessionLocal, ProcessedOrder, Stock

load_dotenv()  # Load environment variables from .env file

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.getLogger("kafka").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

consumer = KafkaConsumer(
    "orders",
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    group_id="stock_service",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)

for message in consumer:
    order = message.value
    order_id = order.get("order_id")

    if order_id is None:
        logger.warning(f"Received order: {order} without order_id. Skipping.")
        continue

    with SessionLocal() as session:
        try:
            session.add(ProcessedOrder(order_id=order_id))
            stock_item = session.get(Stock, order["name"])

            if stock_item is None:
                session.commit()  # Commit the ProcessedOrder to avoid reprocessing
                logger.warning(
                    f"Stock item '{order['name']}' not found. Skipping order {order_id}."
                )
                continue

            if stock_item.quantity < order["quantity"]:
                session.commit()  # Commit the ProcessedOrder to avoid reprocessing
                logger.warning(
                    f"Insufficient stock for '{order['name']}'. Order {order_id} cannot be processed."
                )
                continue

            stock_item.quantity -= order["quantity"]
            session.commit()
            logger.info(
                f"Order {order_id} - {order['name']}: {order['quantity']}x removed. "
                f"{stock_item.quantity} left."
            )

        except IntegrityError:
            session.rollback()
            logger.warning(f"Order {order_id} has already been processed. Skipping.")
