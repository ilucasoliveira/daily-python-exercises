import json
import logging

from kafka import KafkaConsumer
from sqlalchemy.exc import IntegrityError

from database import SessionLocal, ProcessedOrder, Stock

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.getLogger("kafka").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

consumer = KafkaConsumer(
    "orders",
    bootstrap_servers="localhost:9092",
    group_id="stock_group",
    auto_offset_reset="earliest",
)

for message in consumer:
    order = json.loads(message.value.decode("utf-8"))
    order_id = order.get("order_id")

    if order_id is None:
        logger.warning(f"order without id ignored: {order}")
        continue

    with SessionLocal() as session:
        try:
            session.add(ProcessedOrder(order_id=order_id))

            product = session.get(Stock, order["name"])

            if product is None:
                session.commit()
                logger.warning(
                    f"order {order_id}: product {order['name']} not found, rejected"
                )
                continue

            if product.quantity < order["quantity"]:
                session.commit()
                logger.warning(
                    f"order {order_id}: not enough {order['name']} "
                    f"(requested {order['quantity']}, available {product.quantity}), rejected"
                )
                continue

            product.quantity -= order["quantity"]
            session.commit()
            logger.info(
                f"order {order_id}: {order['quantity']}x {order['name']} removed, "
                f"{product.quantity} left"
            )

        except IntegrityError:
            session.rollback()
            logger.warning(f"duplicate order {order_id} ignored")
