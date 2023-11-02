import os
import sys
import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        "localhost", credentials=pika.PlainCredentials("user", "bitnami")
    )
)
channel = connection.channel()
channel.queue_declare(queue="new_hello", durable=True)


def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")
    time.sleep(body.count(b"."))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="new_hello", on_message_callback=callback)
print("[x] Waiting for messages. To exit press CTRL-C")
channel.start_consuming()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit()
