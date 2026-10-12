# Cria a pasta day-063 e copia pra ela o docker-compose.yml do day-062 (o Kafka é o mesmo).
# O container já está rodando, então não precisa subir de novo.

# Exercício 1: producer.py que manda 10 mensagens
# Em vez de um hello kafka só, ele manda:
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
    logger.info(f"message {i} created!")

producer.flush()
