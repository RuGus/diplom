# -*- coding: utf-8 -*-
"""Параметры окружения.

Attributes:
    RMQ_USER (str): Логин RMQ
    RMQ_PASSWORD (str): Пароль RMQ
    RMQ_HOST (str): Хост RMQ
    RMQ_PORT (int): Порт RMQ
    RMQ_WORKLOAD_QUEUE (str): Название очереди с запросами
    MINIO_ROOT_USER (str): Пользователь Minio
    MINIO_ROOT_PASSWORD (str): Пароль Minio
    MINIO_HOST (str): Хост Minio
    MINIO_PORT (int): Порт Minio
    TMP_DIR (str): Папка для временных файлов внутри контейнера
    PROCESSED_DIR (str): Название папки для результатов в S3
    OPENSSL_PATH (str): Путь до openssl
    CERT_PATH (str): Путь к сертификату
    KEY_PATH (str): Путь к ключу
    WORKERS_COUNT (int): Количество обработчиков
    LOG_LEVEL (str): Уровень логгирования

"""
import os

RMQ_USER = os.environ.get("RMQ_USER", "user")
RMQ_PASSWORD = os.environ.get("RMQ_PASSWORD", "bitnami")
RMQ_HOST = os.environ.get("RMQ_HOST", "rabbit_node")
RMQ_PORT = int(os.environ.get("RMQ_PORT", 5672))
RMQ_WORKLOAD_QUEUE = os.environ.get("RMQ_WORKLOAD_QUEUE", "crypto_process")
MINIO_ROOT_USER = os.environ.get("MINIO_ROOT_USER", "admin")
MINIO_ROOT_PASSWORD = os.environ.get("MINIO_ROOT_PASSWORD", "minio#123")
MINIO_HOST = os.environ.get("MINIO_HOST", "minio")
MINIO_PORT = int(os.environ.get("MINIO_PORT", 9000))
TMP_DIR = os.environ.get("TMP_DIR", "/tmp/")
PROCESSED_DIR = os.environ.get("PROCESSED_DIR", "processed/")
OPENSSL_PATH = os.environ.get("OPENSSL_PATH", "/usr/bin/openssl")
CERT_PATH = os.environ.get("CERT_PATH", "/usr/src/crypto_hub/demo_certs/cert.pem")
KEY_PATH = os.environ.get("KEY_PATH", "/usr/src/crypto_hub/demo_certs/private.pem")
WORKERS_COUNT = int(os.environ.get("WORKERS_COUNT", 2))
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
