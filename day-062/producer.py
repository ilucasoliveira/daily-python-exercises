from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers="localhost:9092")

producer.send("messages", "hello kafka".encode())
producer.flush()
