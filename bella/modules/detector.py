#!/usr/bin/env python3


def is_int(val=None):
    try:
        return int(val) == val
    except Exception:
        return False


def is_num(val=None):
    try:
        return float(val) == val
    except Exception:
        return False


def is_float(val=None):
    return is_num(val) and not is_int(val)


def is_str(val=None):
    try:
        return str(val) == val
    except Exception:
        return False


def is_list(val=None):
    try:
        return isinstance(val, list)
    except Exception:
        return False


def is_dict(val=None):
    try:
        return isinstance(val, dict)
    except Exception:
        return False
