import pika
from settings import (
    RMQ_HOST,
    RMQ_PASSWORD,
    RMQ_PORT,
    RMQ_USER,
)


def get_rmq_connection():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            RMQ_HOST,
            RMQ_PORT,
            credentials=pika.PlainCredentials(RMQ_USER, RMQ_PASSWORD),
        )
    )
    return connection
