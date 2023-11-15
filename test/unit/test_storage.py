import unittest
from unittest.mock import Mock, patch, MagicMock

from src.storage import del_file, get_file, get_s3_client, put_file


TEST_BUCKET = "test_bucket"
TEST_OBJECT = "test_object"
TEST_FILE = "test_file"


class TestStorage(unittest.TestCase):
    @patch("src.storage.MINIO_HOST", "TEST_MINIO_HOST")
    @patch("src.storage.MINIO_ROOT_USER", "TEST_MINIO_ROOT_USER")
    @patch("src.storage.MINIO_PORT", "TEST_MINIO_PORT")
    @patch("src.storage.MINIO_ROOT_PASSWORD", "TEST_MINIO_ROOT_PASSWORD")
    @patch("src.storage.minio.Minio")
    def test_get_s3_client(self, minio: Mock):
        minio.return_value = "test_connection"
        test_connection = get_s3_client()
        minio.assert_called_once_with(
            "TEST_MINIO_HOST:TEST_MINIO_PORT",
            access_key="TEST_MINIO_ROOT_USER",
            secret_key="TEST_MINIO_ROOT_PASSWORD",
            secure=False,
        )
        self.assertEqual(test_connection, "test_connection")

    def test_get_file(self):
        client = MagicMock()
        client.fget_object = Mock()
        get_file(client, TEST_BUCKET, TEST_OBJECT, TEST_FILE)
        client.fget_object.assert_called_once_with(
            bucket_name=TEST_BUCKET, object_name=TEST_OBJECT, file_path=TEST_FILE
        )

    def test_put_file(self):
        client = MagicMock()
        client.fput_object = Mock()
        put_file(client, TEST_BUCKET, TEST_OBJECT, TEST_FILE)
        client.fput_object.assert_called_once_with(
            bucket_name=TEST_BUCKET, object_name=TEST_OBJECT, file_path=TEST_FILE
        )

    def test_del_file(self):
        client = MagicMock()
        client.remove_object = Mock()
        del_file(client, TEST_BUCKET, TEST_OBJECT)
        client.remove_object.assert_called_once_with(
            bucket_name=TEST_BUCKET, object_name=TEST_OBJECT
        )
