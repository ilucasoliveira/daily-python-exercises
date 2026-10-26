import json
import logging
from fastapi import FastAPI
from kafka import KafkaProducer
from datetime import datetime, timezone


class JsonFormatter(logging.Formatter):
    def format(self, record):
        dict_format = {
            "level": record.levelname,
            "message": record.getMessage(),
            "@timestamp": datetime.fromtimestamp(
                record.created, tz=timezone.utc
            ).isoformat(),
        }
        return json.dumps(dict_format)


class KafkaHandler(logging.Handler):
    def emit(self, record):
        message = self.format(record)
        producer.send("app-logs", message)


producer = KafkaProducer(
    bootstrap_servers="localhost:9092", value_serializer=lambda v: v.encode("utf-8")
)


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())

kafka_handler = KafkaHandler()
kafka_handler.setFormatter(JsonFormatter())

logger.addHandler(handler)
logger.addHandler(kafka_handler)


app = FastAPI()


@app.get("/health")
def health_check():
    logger.info("server is healthy")
    return {"status": "OK"}


@app.get("/error_zero")
def division_by_zero():
    try:
        error = 10 / 0
    except ZeroDivisionError as e:
        logger.error("division by zero is incorrect!")
        return {"message": str(e)}
