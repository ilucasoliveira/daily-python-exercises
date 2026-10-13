import logging
from kafka import KafkaProducer

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.getLogger("kafka").setLevel(logging.WARNING)
logger = logging.getLogger()

producer = KafkaProducer(bootstrap_servers="localhost:9092")

for i in range(1, 11):
    producer.send("receives", f"message {i}".encode())
    logging.info(f"message {i} created!")

producer.flush()
