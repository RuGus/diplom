from asyncio import sleep
import uuid
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
        self.channel.queue_declare(RMQ_WORKLOAD_QUEUE)

    def call(self, msg):
        self.channel.basic_publish("", RMQ_WORKLOAD_QUEUE, msg)


exchnge = AMQP_Exchnge()
for i in range(5):
    exchnge.call(str(i))