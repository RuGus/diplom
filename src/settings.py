# -*- coding: utf-8 -*-
"""Параметры окружения.

Attributes:
    RMQ_USER (): 
    RMQ_PASSWORD (): 
    RMQ_HOST (): 
    RMQ_PORT (): 
    RMQ_WORKLOAD_QUEUE (): 
    MINIO_ROOT_USER (): 
    MINIO_ROOT_PASSWORD (): 
    MINIO_HOST (): 
    MINIO_PORT (): 
    TMP_DIR (): 
    PROCESSED_DIR (): 
    OPENSSL_PATH (): 
    CERT_PATH (): 
    KEY_PATH (): 
    WORKERS_COUNT (): 

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
