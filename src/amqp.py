import pika
from settings import (
    RMQ_HOST,
    RMQ_PORT,
    RMQ_USER,
    RMQ_PASSWORD,
    RMQ_VHOST,
    RMQ_RESULT_QUEUE,
    RMQ_WORKLOAD_QUEUE,
)


class AMQP_Exchnge:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                RMQ_HOST,
                RMQ_PORT,
                credentials=pika.PlainCredentials(RMQ_USER, RMQ_PASSWORD),
            )
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(RMQ_RESULT_QUEUE)
        self.channel.queue_declare(RMQ_WORKLOAD_QUEUE)
        self.channel.basic_qos(prefetch_count=1)

    def get_job(self):
        method, props, body = self.channel.basic_get(RMQ_WORKLOAD_QUEUE, auto_ack=True)
        return body

    def put_result(self, msg):
        self.channel.basic_publish("", RMQ_RESULT_QUEUE, msg)


exchnge = AMQP_Exchnge()
body = exchnge.get_job()
exchnge.put_result("processed" + str(body))
