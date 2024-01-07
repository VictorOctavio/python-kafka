import json
from kafka import KafkaProducer

if __name__ == '__main__':
    print("Starting kafka producer..")
    producer = KafkaProducer(
        bootstrap_servers="localhost:9092",
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
    # Topic, Value
    producer.send("auth", "first auth test")
    producer.flush()
    print("message produced successfully")

# TOPIC_NAME = 'orders'

# if __name__ == '__main__':
#     print("Starting kafka producer..")
#     producer = KafkaProducer(
#         bootstrap_servers="localhost:9092",
#         value_serializer=lambda v: json.dumps(v).encode("utf-8")
#     )
#     # Topic, Value
#     producer.send("auth", "auth test")
#     producer.flush()
#     print("message produced successfully")
