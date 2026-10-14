import logging
from kafka import KafkaConsumer

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.getLogger("kafka").setLevel(logging.WARNING)
logging.getLogger("watchfiles").setLevel(logging.WARNING)
logger = logging.getLogger()

consumer = KafkaConsumer(
    "orders",
    bootstrap_servers="localhost:9092",
    group_id="counter_group",
    auto_offset_reset="earliest",
)

counter = 1

for order in consumer:
    logger.info(f"order {counter}: {order.value.decode()}")
    counter += 1
