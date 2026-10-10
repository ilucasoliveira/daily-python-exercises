import logging
from kafka import KafkaConsumer

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()

consumer = KafkaConsumer("messages", bootstrap_servers="localhost:9092")
for message in consumer:
    logger.info(message.value.decode())
