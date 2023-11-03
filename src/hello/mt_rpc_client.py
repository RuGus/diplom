import random
import pika
import uuid
from concurrent.futures import ThreadPoolExecutor


class FibonacciRpcClient(object):
    def __init__(self, n):
        print(f" [x] Requesting fib({n})")
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                "localhost", credentials=pika.PlainCredentials("user", "bitnami")
            )
        )

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue="", exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True,
        )

        self.response = None
        self.corr_id = None

        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange="",
            routing_key="rpc_queue",
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(n),
        )
        self.connection.process_data_events(time_limit=None)
        print(f"[.] For {n=} got {int(self.response)}")

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body


with ThreadPoolExecutor(4) as executor:
    executor.map(FibonacciRpcClient, [random.randint(30,35) for i in range(100)])