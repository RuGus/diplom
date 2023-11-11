import json
import pika
import uuid


class RpcClient(object):
    def __init__(self, json_rpc_request):
        print(f" [x] Requesting \n{json_rpc_request=}\n\n\n")
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
        print(f"For \n{json_rpc_request=}\n got \n{str(self.response)}\n")

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body


a = {
    "jsonrpc": "2.0",
    "method": "pack_sgn_enc",
    "params": ["pack-sgn-enc", "file.txt"],
    "id": "UID",
}
json_rpc_request = json.dumps(a)

RpcClient(json_rpc_request)
