import os

from minio import Minio

MINIO_ROOT_USER = os.environ.get("MINIO_ROOT_USER")
MINIO_ROOT_PASSWORD = os.environ.get("MINIO_ROOT_PASSWORD")
MINIO_HOST = os.environ.get("MINIO_HOST", "minio")
MINIO_PORT = int(os.environ.get("MINIO_PORT", 9000))
BUCKET = "new-bucket"
FILES_COUNT = 100

s3_client = Minio(
    f"{MINIO_HOST}:{MINIO_PORT}",
    access_key=MINIO_ROOT_USER,
    secret_key=MINIO_ROOT_PASSWORD,
    secure=False,
)
if not s3_client.bucket_exists(BUCKET):
    s3_client.make_bucket(BUCKET)

for i in range(FILES_COUNT):
    file_name = f"{i}.txt"
    with open(file_name, "w") as file:
        file.write(str(i))
    s3_client.fput_object(
        bucket_name=BUCKET, object_name=file_name, file_path=file_name
    )
    os.remove(file_name)
