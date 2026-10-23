import json
import logging

from elasticsearch import Elasticsearch
from datetime import datetime, timezone

es = Elasticsearch("http://localhost:9200")


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {
            "level": record.levelname,
            "message": record.getMessage(),
            "name": record.name,
            "@timestamp": datetime.fromtimestamp(
                record.created, tz=timezone.utc
            ).isoformat(),
        }
        return json.dumps(log_entry)


class ElasticsearchHandler(logging.Handler):
    def emit(self, record):
        json_message = self.format(record)
        dict_message = json.loads(json_message)
        es.index(index="app-logs", document=dict_message)


handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())

logging.basicConfig(level=logging.INFO, handlers=[handler])
logger = logging.getLogger(__name__)

es_handler = ElasticsearchHandler()
es_handler.setFormatter(JsonFormatter())

logger.addHandler(es_handler)

logger.info("order created")  # tests
logger.error("payment failed")  # tests
