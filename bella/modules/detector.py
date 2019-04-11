#!/usr/bin/env python3

from urllib.parse import urlparse


def is_int(val=None):
    try:
        return int(val) == val
    except Exception as err:
        print(err)
        pass
    return False


def is_num(val=None):
    try:
        return float(val) == val
    except Exception as err:
        print(err)
        pass
    return False


def is_float(val=None):
    return is_num(val) and not is_int(val)


def is_str(val=None):
    try:
        return str(val) == val
    except Exception as err:
        print(err)
        pass
    return False


def is_list(val=None):
    try:
        return isinstance(val, list)
    except Exception as err:
        print(err)
        pass
    return False


def is_dict(val=None):
    try:
        return isinstance(val, dict)
    except Exception as err:
        print(err)
        pass
    return False


def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc, result.path])
    except Exception as err:
        print(err)
        pass
    return False
