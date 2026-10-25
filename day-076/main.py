import random
from datetime import datetime, timezone
from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")
es.indices.delete(index="app-logs", ignore_unavailable=True)

info = es.info()
print(info["version"]["number"])

counter = 0
error_counter = 0
while counter != 20:
    random_level = random.choice(["INFO", "WARNING", "ERROR"])
    if random_level == "ERROR":
        error_counter += 1
    es.index(
        index="app-logs",
        document={
            "@timestamp": datetime.now(timezone.utc).isoformat(),
            "level": random_level,
            "message": "this is a test!",
        },
    )
    counter += 1

print("TOTAL ERROR: ", error_counter)
