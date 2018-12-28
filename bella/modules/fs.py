#!/usr/bin/env python3

from os import path, remove as rmfile
from shutil import copytree, copy2, rmtree as rmdir


def remove(f):
    try:
        if path.exists(f):
            if path.isdir(f):
                return rmdir(f, ignore_errors=True)
            else:
                return rmfile(f)
    except Exception as e:
        pass
    return False


def copy(source, dest):
    try:
        if path.exists(source):
            if path.isdir(source):
                return copytree(source, dest)
            else:
                return copy2(source, dest)
    except Exception as e:
        pass
    return True
