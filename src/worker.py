import os
import threading

import pika
from crypto import apply_pipline
from rpc import get_error_responce, get_params_from_request, get_result_responce
from settings import (
    PROCESSED_DIR,
    RMQ_HOST,
    RMQ_PASSWORD,
    RMQ_PORT,
    RMQ_USER,
    RMQ_WORKLOAD_QUEUE,
    TMP_DIR,
)
from storage import get_file, get_s3_client, put_file


class CryptoHubWorker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                RMQ_HOST,
                RMQ_PORT,
                credentials=pika.PlainCredentials(RMQ_USER, RMQ_PASSWORD),
            )
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=RMQ_WORKLOAD_QUEUE)
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(
            queue=RMQ_WORKLOAD_QUEUE, on_message_callback=self.on_request
        )
        self.s3_client = get_s3_client()

    def run(self):
        self.channel.start_consuming()

    def workload(self, request_body):
        try:
            request_id, pipline, bucket_name, object_name = get_params_from_request(
                request_body
            )
            # Получить объект
            source_file_name = TMP_DIR + object_name
            if os.path.exists(source_file_name):
                os.remove(source_file_name)
            get_file(self.s3_client, bucket_name, object_name, source_file_name)
            # Выполнить операции
            result_file_path = apply_pipline(pipline, source_file_name)
            result_object_name = os.path.basename(result_file_path)
            # Запушить файл
            result_bucket_name = bucket_name + PROCESSED_DIR
            put_file(self.s3_client, result_bucket_name, object_name, result_file_path)
            # Сформировать ответ
        except Exception as exc:
            return get_error_responce(str(exc))
        return get_result_responce(result_bucket_name, result_object_name, request_id)

    def on_request(self, ch, method, props, body):
        response = self.workload(body)
        ch.basic_publish(
            exchange="",
            routing_key=props.reply_to,
            properties=pika.BasicProperties(correlation_id=props.correlation_id),
            body=str(response),
        )
        ch.basic_ack(delivery_tag=method.delivery_tag)
