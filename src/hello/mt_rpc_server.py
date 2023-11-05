import pika, time, threading


class Threaded_worker(threading.Thread):
    def __init__(self, worker_id):
        self.worker_id = worker_id
        threading.Thread.__init__(self)
        print(f"Worker {self.worker_id} start")
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                "localhost", credentials=pika.PlainCredentials("user", "bitnami")
            )
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue="rpc_queue")
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(
            queue="rpc_queue", on_message_callback=self.on_request
        )
    def run(self):

        print(" [x] Awaiting RPC requests")
        self.channel.start_consuming()

    def fib(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)

    def on_request(self, ch, method, props, body):
        n = int(body)

        print(f" [.] {self.worker_id=} fib({n})")
        response = self.fib(n)

        ch.basic_publish(
            exchange="",
            routing_key=props.reply_to,
            properties=pika.BasicProperties(correlation_id=props.correlation_id),
            body=str(response),
        )
        ch.basic_ack(delivery_tag=method.delivery_tag)


for i in range(5):
    worker_tread = Threaded_worker(i)
    worker_tread.start()
