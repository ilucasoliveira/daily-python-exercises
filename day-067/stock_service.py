import json
import logging

from database import SessionLocal, ProcessedOrder
from kafka import KafkaConsumer
from sqlalchemy.exc import IntegrityError

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.getLogger("kafka").setLevel(logging.WARNING)
logger = logging.getLogger()

consumer = KafkaConsumer(
    "orders",
    bootstrap_servers="localhost:9092",
    group_id="stock_group",
    auto_offset_reset="earliest",
)

for message in consumer:
    dict_order = json.loads(message.value.decode())
    order_id = dict_order.get("order_id")

    if order_id is None:
        logger.warning("ID order: None not found")
        continue

    with SessionLocal() as session:
        try:
            new_order_id = ProcessedOrder(order_id=order_id)
            session.add(new_order_id)
            session.commit()
            logger.info(
                f"order {order_id}: {dict_order['quantity']}X {dict_order['name']} removed from stock"
            )
        except IntegrityError:
            session.rollback()
            logger.warning(f"ID order: {order_id} duplicated")
