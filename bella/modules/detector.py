#!/usr/bin/env python3

from typing import Any
from urllib.parse import urlparse


def is_int(val: Any):
    try:
        return int(val) == val and '.' not in str(val)
    except Exception:
        pass
    return False


def is_num(val: Any):
    try:
        return float(val) == val
    except Exception:
        pass
    return False


def is_float(val: Any):
    return is_num(val) and not is_int(val)


def is_str(val: Any):
    try:
        return str(val) == val
    except Exception:
        pass
    return False


def is_bool(val: Any):
    return val is True or val is False


def is_list(val: Any):
    try:
        return isinstance(val, list)
    except Exception:
        pass
    return False


def is_dict(val: Any):
    try:
        return isinstance(val, dict)
    except Exception:
        pass
    return False


def is_valid_url(url: str):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        pass
    return False
