#!/usr/bin/env python3

from os import path, remove as rmfile
from shutil import copytree, copy2, rmtree as rmdir

from glob import glob

from .logger import log


def exists(f: str):
    return path.exists(f)


def isdir(f: str):
    return path.isdir(f)


def isfile(f: str):
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
