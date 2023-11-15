import json
import unittest

from src.rpc import (
    get_error_responce,
    get_params_from_request,
    get_result_responce,
    is_valid_rpc_request,
)

TEST_ERR_MSG = "test_error"
TEST_ERR_CODE = 404
TEST_BUCKET = "test_bucket"
TEST_OBJECT = "test_object"
TEST_ID = "test_id"
TEST_PIPLINE = "pack_sgn_enc"
VALID_REQUEST = json.dumps(
    {
        "jsonrpc": "2.0",
        "method": TEST_PIPLINE,
        "params": [TEST_BUCKET, TEST_OBJECT],
        "id": TEST_ID,
    }
)
INVALID_REQUEST = ""


class TestRPC(unittest.TestCase):
    def test_is_valid_rpc_request(self):
        self.assertTrue(is_valid_rpc_request(VALID_REQUEST))
        self.assertFalse(is_valid_rpc_request(INVALID_REQUEST))

    def test_get_params_from_request(self):
        request_id, pipline, bucket_name, object_name = get_params_from_request(
            VALID_REQUEST
        )
        self.assertEqual(request_id, TEST_ID)
        self.assertEqual(pipline, TEST_PIPLINE)
        self.assertEqual(bucket_name, TEST_BUCKET)
        self.assertEqual(object_name, TEST_OBJECT)
        with self.assertRaises(Exception) as context:
            get_params_from_request(INVALID_REQUEST)

    def test_get_result_responce(self):
        responce = get_result_responce(TEST_BUCKET, TEST_OBJECT, TEST_ID)
        self.assertEqual(
            responce,
            '{"jsonrpc": "2.0", "result": {"bucket_name": "test_bucket", "object_name": "test_object"}, "id": "test_id"}',
        )

    def test_get_error_responce(self):
        responce = get_error_responce(TEST_ERR_MSG, TEST_ID, TEST_ERR_CODE)
        self.assertEqual(
            responce,
            '{"jsonrpc": "2.0", "error": {"code": 404, "message": "test_error"}, "id": "test_id"}',
        )
