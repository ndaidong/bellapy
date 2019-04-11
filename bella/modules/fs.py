#!/usr/bin/env python3

from os import path, remove as rmfile
from shutil import copytree, copy2, rmtree as rmdir
from json import dumps, load


def exists(f):
    return path.exists(f)


def isdir(f):
    return path.isdir(f)


def remove(f):
    try:
        if exists(f):
            if isdir(f):
                return rmdir(f, ignore_errors=True)
            else:
                return rmfile(f)
    except Exception as err:
        print(err)
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
        print(err)
        pass
    return True


def write_json_to_file(file, data):
    try:
        jstr = dumps(data, indent=2, sort_keys=False)
        with open(file, 'w+') as write_file:
            write_file.write(jstr)
        return True
    except Exception as err:
        print(err)
        pass
    return False


def read_json_from_file(file):
    try:
        if exists(file):
            with open(file, 'r') as read_file:
                return load(read_file)
    except Exception as err:
        print(err)
        pass
    return {}
