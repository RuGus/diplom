import pika
import sys


connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        "localhost", credentials=pika.PlainCredentials("user", "bitnami")
    )
)
channel = connection.channel()
channel.queue_declare(queue="new_hello", durable=True)
message = " ".join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
    exchange="",
    routing_key="new_hello",
    body=message,
    properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE),
)
print(f"[x] Sent {message}")
connection.close()
