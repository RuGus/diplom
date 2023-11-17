"""Модуль работы с хранилищем"""
import minio

from src.logs import logger
from src.settings import MINIO_HOST, MINIO_PORT, MINIO_ROOT_PASSWORD, MINIO_ROOT_USER


def get_s3_client():
    s3_client = minio.Minio(
        f"{MINIO_HOST}:{MINIO_PORT}",
        access_key=MINIO_ROOT_USER,
        secret_key=MINIO_ROOT_PASSWORD,
        secure=False,
    )
    return s3_client


def get_file(client: minio.Minio, bucket_name: str, object_name: str, file_path: str):
    client.fget_object(
        bucket_name=bucket_name, object_name=object_name, file_path=file_path
    )


def put_file(client: minio.Minio, bucket_name: str, object_name: str, file_path: str):
    logger.debug(f"{bucket_name=}, {object_name=}, {file_path=}")
    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)
    client.fput_object(
        bucket_name=bucket_name, object_name=object_name, file_path=file_path
    )


def del_file(client: minio.Minio, bucket_name: str, object_name: str):
    client.remove_object(bucket_name=bucket_name, object_name=object_name)
