# No day-064/consumer.py, adiciona o group_id no KafkaConsumer(...), junto dos parâmetros que já estão lá. Mantém o earliest.
# O experimento, nessa ordem:
# Roda o consumer. Anota quantas mensagens ele leu
# Espera uns 10 segundos antes do Ctrl+C (te explico o porquê depois)
# Ctrl+C
# Roda o producer (10 mensagens novas)
# Roda o consumer de novo
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
    group_id="counter-group",
    auto_offset_reset="earliest",
)

counter = 1

for receive in consumer:
    logger.info(f"receives {counter}: {receive.value.decode()}")
    counter += 1
