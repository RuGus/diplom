from minio import Minio
from minio.error import S3Error
from settings import MINIO_ROOT_PASSWORD, MINIO_HOST, MINIO_PORT, MINIO_ROOT_USER


def get_s3_client():
    s3_client = Minio(
        f"{MINIO_HOST}:{MINIO_PORT}",
        access_key=MINIO_ROOT_USER,
        secret_key=MINIO_ROOT_PASSWORD,
        secure=False,
    )
    return s3_client


def get_file(client: Minio, bucket_name, object_name, file_path):
    client.fget_object(
        bucket_name=bucket_name, object_name=object_name, file_path=file_path
    )


def put_file(client: Minio, bucket_name, object_name, file_path):
    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)
    client.fput_object(
        bucket_name=bucket_name, object_name=object_name, file_path=file_path
    )


def del_file(client: Minio, bucket_name, object_name):
    client.remove_object(bucket_name=bucket_name, object_name=object_name)
