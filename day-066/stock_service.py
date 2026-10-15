import json
import logging

from kafka import KafkaConsumer

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

processed_ids = set()
processed_ids.add("x")


for message in consumer:
    order = json.loads(message.value.decode())
    order_id = order.get("order_id")

    if order_id is None:
        logger.warning(f"order without id ignored: {order}")
        continue

    if order_id in processed_ids:
        logger.warning(f"duplicate order {order_id} ignored")
        continue

    logger.info(f"removing {order['quantity']}X {order['item']} from stock")
    processed_ids.add(order_id)
