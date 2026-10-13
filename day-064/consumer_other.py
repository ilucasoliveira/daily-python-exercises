# A regra completa do dia, em duas linhas:
# mesmo grupo: divide o trabalho (e um cobre o outro se cair)
# grupos diferentes: cada um recebe tudo, independente

# Por que isso é o coração do Kafka
# Pensa numa loja. Acontece um evento: “pedido 123 criado”. Um único producer publica isso no topic orders. Aí:

# o grupo email-service lê e manda o email de confirmação
# o grupo stock-service lê e baixa o estoque
# o grupo analytics lê e atualiza o dashboard
import logging
from kafka import KafkaConsumer

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.getLogger("kafka").setLevel(logging.WARNING)
logger = logging.getLogger()

consumer = KafkaConsumer(
    "receives",
    bootstrap_servers="localhost:9092",
    group_id="other-group",
    auto_offset_reset="earliest",
)

counter = 1

for receive in consumer:
    logger.info(f"receives {counter}: {receive.value.decode()}")
    counter += 1
