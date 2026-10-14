# Exercício 2: os dois serviços da loja
# Dois arquivos novos, dois consumers, cada um num grupo diferente, os dois lendo o topic "orders":
# email_service.py: pra cada pedido, loga algo como sending confirmation email: 10x apple
# stock_service.py: pra cada pedido, loga algo como removing 10 apple from stock
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
    group_id="email_group",
    auto_offset_reset="earliest",
)

for message in consumer:
    order = json.loads(message.value.decode())
    logger.info(f"sending confirmation email: {order['quantity']}x {order['item']}")
