#!/usr/bin/env python3

from os import path, remove as rmfile
from shutil import copytree, copy2, rmtree as rmdir
from json import dumps, load
from glob import glob

from .logger import log


def exists(f):
    return path.exists(f)


def isdir(f):
    return path.isdir(f)


def isfile(f):
    return path.isfile(f)


def get_files(pattern):
    return glob(pattern)


def remove(f):
    try:
        if exists(f):
            if isdir(f):
                return rmdir(f, ignore_errors=True)
            else:
                return rmfile(f)
    except Exception as err:
        log('remove', f, err)
        pass
    return False


def copy(source, dest):
    try:
        if exists(source):
            if isdir(source):
                return copytree(source, dest)
            else:
                return copy2(source, dest)
    except Exception as err:
        log('copy', 'from', source, 'to', dest, err)
        pass
    return True


def write_json_to_file(file_path: str = '', data: dict = {}):
    try:
        jstr = dumps(data, indent=2, sort_keys=True, ensure_ascii=False)
        with open(file_path, 'w') as write_file:
            write_file.write(jstr)
            write_file.flush()
        return True
    except Exception as err:
        log('write_json_to_file', file_path, err)
        pass
    return False


def read_json_from_file(file_path: str = ''):
    try:
        if exists(file_path):
            with open(file_path, 'r') as read_file:
                return load(read_file)
    except Exception as err:
        log('read_json_from_file', file_path, err)
        pass
    return {}
