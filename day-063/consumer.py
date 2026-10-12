# Exercício 2: consumer.py que conta
# O consumer lê do mesmo topic messages e loga cada mensagem junto com quantas já recebeu:
import logging
from kafka import KafkaConsumer

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.getLogger("kafka").setLevel(logging.WARNING)
logger = logging.getLogger()

consumer = KafkaConsumer(
    "receives", bootstrap_servers="localhost:9092", auto_offset_reset="earliest"
)

counter = 1

for receive in consumer:
    logger.info(f"receives {counter}: {receive.value.decode()}")
    counter += 1
