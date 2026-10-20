import json
import logging

from dotenv import load_dotenv
from kafka import KafkaConsumer
from sqlalchemy.exc import IntegrityError

from database import SessionLocal, ProcessedOrder, Stock

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.getLogger("kafka").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

consumer = KafkaConsumer(
    "orders", group_id="stock_group", bootstrap_servers="localhost:9092"
)

for message in consumer:
    order = json.loads(message.value.decode())
    order_id = order.get("order_id")

    if order_id is None:
        logger.warning(f"Received order: {order} without order_id. Skipping.")
        continue

    with SessionLocal() as session:
        try:
            session.add(ProcessedOrder(order_id=order_id))
            stock_item = session.get(Stock, order["name"])

            if stock_item is None:
                session.commit()
                logger.warning(
                    f"Stock item '{order['name']}' not found. Skipping order {order_id}."
                )
                continue

            if stock_item.quantity < order["quantity"]:
                session.commit()
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
