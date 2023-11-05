import json
from jsonschema.validators import validate

RPC_REQUEST_SCHEMA = {
    "type": "object",
    "properties": {
        "jsonrpc": {"type": "string"},
        "method": {"type": "string"},  # pipline
        "params": {
            "type": "array",
            "prefixItems": [
                {"type": "string"},  # bucket_name
                {"type": "string"},  # object_name
            ],
            "items": False,
        },
        "id": {"type": "string"},  # UID
    },
    "required": ["jsonrpc", "method", "params", "id"],
    "additionalProperties": False,
}


def is_valid_rpc_request(request_body: str):
    try:
        request_dict = json.loads(request_body)
        validate(instance=request_dict, schema=RPC_REQUEST_SCHEMA)
    except Exception as exc:
        return False
    return True


def get_params_from_request(request_body: str):
    if is_valid_rpc_request(request_body):
        request_dict = json.loads(request_body)
        pipline = request_dict["method"]
        request_id = request_dict["id"]
        bucket_name, object_name = request_dict["params"]
        return request_id, pipline, bucket_name, object_name
    else:
        raise Exception("Invalid rpc request")


def get_error_responce(err_msg: str, request_id=None, err_code=-32600):
    responce_dict = {
        "jsonrpc": "2.0",
        "error": {"code": err_code, "message": err_msg},
        "id": request_id,
    }
    return json.dumps(responce_dict)


def get_result_responce(bucket_name: str, object_name: str, request_id: str):
    responce_dict = {
        "jsonrpc": "2.0",
        "result": {
            "bucket_name": bucket_name,
            "object_name": object_name,
        },
        "id": request_id,
    }
    return json.dumps(responce_dict)
