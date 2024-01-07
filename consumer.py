import json
from kafka import KafkaConsumer

if __name__ == '__main__':
    consumer = KafkaConsumer(
        "auth",
        bootstrap_servers = "localhost:9092",
        value_deserializer = lambda m: json.loads(m.decode('ascii'))
    )
    for message in consumer:
        print("Message Received: " + message.value)

# if __name__ == '__main__':
#     consumer = KafkaConsumer(
#         'auth',
#         bootstrap_servers="localhost:9092",
#         value_deserializer=lambda m: json.loads(m.decode('ascii'))
#     )
#     for message in consumer:
#         print("New User Received: " + str(message.value))


# import json
# from kafka import KafkaConsumer

# TOPIC_NAME = 'orders'

# if __name__ == '__main__':
#     consumer = KafkaConsumer(
#         'orders',
#         bootstrap_servers = "localhost:9092",
#         value_deserializer = lambda m: json.loads(m.decode('ascii'))
#     )
#     for message in consumer:
#         print("Message Received: " + message.value)
        