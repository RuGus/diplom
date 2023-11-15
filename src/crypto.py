import os
from copy import copy
from subprocess import PIPE, Popen
from zipfile import ZIP_DEFLATED, ZipFile

from src.constants.pipelines import PIPELINES
from src.logs import logger
from src.settings import CERT_PATH, KEY_PATH, OPENSSL_PATH


def apply_pipline(pipline, file_path):
    logger.info(f"Start {pipline=} {file_path=}")
    steps = PIPELINES.get(pipline)
    _file_path = copy(file_path)
    if steps:
        for func_name in steps:
            func = globals()[func_name]
            _file_path = func(_file_path)
    return _file_path


def simple_sign_file(file_path):
    logger.info(f"Start with {file_path=}")
    result_file_path = file_path + ".sgn"
    if os.path.exists(result_file_path):
        os.remove(result_file_path)
    cmd_items = (
        OPENSSL_PATH,
        "cms",
        "-sign",
        "-nodetach",
        "-in",
        file_path,
        "-out",
        result_file_path,
        "-signer",
        CERT_PATH,
        "-inkey",
        KEY_PATH,
    )
    logger.debug(f"{cmd_items}")
    process = Popen(cmd_items, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    ret, err = process.communicate()
    os.remove(file_path)
    return result_file_path


def simple_encrypt_file(file_path):
    logger.info(f"Start with {file_path=}")
    result_file_path = file_path + ".enc"
    if os.path.exists(result_file_path):
        os.remove(result_file_path)
    cmd_items = (
        OPENSSL_PATH,
        "cms",
        "-encrypt",
        "-in",
        file_path,
        "-out",
        result_file_path,
        CERT_PATH,
    )
    process = Popen(cmd_items, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    ret, err = process.communicate()
    os.remove(file_path)
    return result_file_path


def simple_pack_file(file_path):
    logger.info(f"Start with {file_path=}")
    result_file_path = file_path + ".zip"
    if os.path.exists(result_file_path):
        os.remove(result_file_path)
    with ZipFile(result_file_path, "w", ZIP_DEFLATED) as zip_dest:
        zip_dest.write(file_path)
    os.remove(file_path)
    return result_file_path
