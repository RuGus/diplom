import unittest
from unittest.mock import Mock, patch

from src.amqp import get_publish_properties, get_rmq_connection


class TestAMQP(unittest.TestCase):
    @patch("src.amqp.RMQ_HOST", "TEST_RMQ_HOST")
    @patch("src.amqp.RMQ_PASSWORD", "TEST_RMQ_PASSWORD")
    @patch("src.amqp.RMQ_PORT", "TEST_RMQ_PORT")
    @patch("src.amqp.RMQ_USER", "TEST_RMQ_USER")
    @patch("src.amqp.pika.BlockingConnection")
    @patch("src.amqp.pika.ConnectionParameters")
    @patch("src.amqp.pika.PlainCredentials")
    def test_get_rmq_connection(
        self, credentials: Mock, connection_params: Mock, connection: Mock
    ):
        credentials.return_value = "test_credentials"
        connection_params.return_value = "test_params"
        connection.return_value = "test_connection"
        test_connection = get_rmq_connection()
        connection.assert_called_once_with("test_params")
        connection_params.assert_called_once_with(
            "TEST_RMQ_HOST", "TEST_RMQ_PORT", credentials="test_credentials"
        )
        credentials.assert_called_once_with("TEST_RMQ_USER", "TEST_RMQ_PASSWORD")
        self.assertEqual(test_connection, "test_connection")

    @patch("src.amqp.pika.BasicProperties")
    def test_get_publish_properties(self, properties: Mock):
        properties.return_value = "test_properties"
        result = get_publish_properties(test="test_value")
        properties.assert_called_once_with(test="test_value")
        self.assertEqual(result, "test_properties")
