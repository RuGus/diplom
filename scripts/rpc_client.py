import copy
import json
import os
import uuid
from concurrent.futures import ThreadPoolExecutor

import pika

RMQ_USER = os.environ.get("RMQ_USER", "user")
RMQ_PASSWORD = os.environ.get("RMQ_PASSWORD", "bitnami")
RMQ_HOST = os.environ.get("RMQ_HOST", "localhost")
RMQ_PORT = int(os.environ.get("RMQ_PORT", 5672))
FILES_COUNT = 100


class RpcClient(object):
    def __init__(self, json_rpc_request):
        print(f"Requesting {json_rpc_request=}\n")
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                RMQ_HOST,
                RMQ_PORT,
                credentials=pika.PlainCredentials(RMQ_USER, RMQ_PASSWORD),
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
            routing_key="crypto_process",
            properties=pika.BasicProperties(
                content_type="application/json",
                content_encoding="utf-8",
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(json_rpc_request),
        )
        self.connection.process_data_events(time_limit=None)
        print(f"Got {self.response.decode('utf-8')}\n")

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body


def get_rpc_request(file_num: int):
    request_dict = {
        "jsonrpc": "2.0",
        "method": "pack_sgn_enc",
        "params": ["new-bucket", f"{file_num}.txt"],
        "id": f"{file_num}",
    }
    return json.dumps(request_dict)


with ThreadPoolExecutor(4) as executor:
    executor.map(RpcClient, [get_rpc_request(num) for num in range(FILES_COUNT)])
