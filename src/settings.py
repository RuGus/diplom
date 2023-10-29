# -*- coding: utf-8 -*-
"""Параметры окружения.

Attributes:
    APP_NAME (str): Название приложения.

"""
import os

RMQ_USER = os.environ.get("RMQ_USER")
RMQ_PASSWORD = os.environ.get("RMQ_PASSWORD")
RMQ_HOST = os.environ.get("RMQ_HOST")
RMQ_PORT = int(os.environ.get("RMQ_PORT"))
RMQ_VHOST = os.environ.get("RMQ_VHOST")
RMQ_LOG = os.environ.get("RMQ_LOG")
RMQ_WORKLOAD_QUEUE = os.environ.get("RMQ_WORKLOAD_QUEUE")
RMQ_RESULT_QUEUE = os.environ.get("RMQ_RESULT_QUEUE")
MINIO_ROOT_USER = os.environ.get("MINIO_ROOT_USER")
MINIO_ROOT_PASSWORD = os.environ.get("MINIO_ROOT_PASSWORD")
