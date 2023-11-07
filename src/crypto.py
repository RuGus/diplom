from subprocess import PIPE, Popen
from constants.pipelines import PIPELINES
from copy import copy


def apply_pipline(pipline, file_path):
    steps = PIPELINES.get(pipline)
    _file_path = copy(file_path)
    if steps:
        for step in steps:
            func_name, func_args = step
            func = globals()[func_name]
            _file_path = func(_file_path, *func_args)
    return _file_path


def sign_file(file_path, *args):
    result_file_path = file_path + ".sgn"
    cmd_items = [
        "mv",
        file_path,
        result_file_path,
    ]
    process = Popen(cmd_items, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    ret, err = process.communicate()
    print(f"{ret=}, {err=}")
    return result_file_path


def encrypt_file(file_path, *args):
    result_file_path = file_path + ".enc"
    cmd_items = [
        "mv",
        file_path,
        result_file_path,
    ]
    process = Popen(cmd_items, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    ret, err = process.communicate()
    print(f"{ret=}, {err=}")
    return result_file_path


def pack_file(file_path, *args):
    result_file_path = file_path + ".zip"
    cmd_items = [
        "mv",
        file_path,
        result_file_path,
    ]
    process = Popen(cmd_items, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    ret, err = process.communicate()
    print(f"{ret=}, {err=}")
    return result_file_path
