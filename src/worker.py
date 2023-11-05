import pika, threading
from src.rpc import get_params_from_request, get_error_responce, get_result_responce


class CryptoHubWorker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
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
        self.channel.start_consuming()

    def workload(self, request_body):
        try:
            request_id, pipline = get_params_from_request(request_body)
            result_file_path = ""
        except Exception as exc:
            return get_error_responce(str(exc))
        return get_result_responce(result_file_path, request_id)

    def on_request(self, ch, method, props, body):
        response = self.workload(body)
        ch.basic_publish(
            exchange="",
            routing_key=props.reply_to,
            properties=pika.BasicProperties(correlation_id=props.correlation_id),
            body=str(response),
        )
        ch.basic_ack(delivery_tag=method.delivery_tag)
