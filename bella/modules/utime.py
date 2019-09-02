#!/usr/bin/env python3

from time import time
from datetime import datetime

from .detector import is_num

PY_DATE_PATTERN = '%Y-%m-%d %H:%M:%S %z'
MY_DATE_PATTERN = '%a, %b %d, %Y %H:%M:%S'


def get_time(ms=False):
    t = time()
    return t if ms is False else int(t)


def format_time(d=datetime.now(), pattern=PY_DATE_PATTERN):
    if is_num(d):
        d = datetime.fromtimestamp(d)
    return d.strftime(pattern)


def get_local_time():
    return format_time(datetime.now())


def get_utc_time():
    return format_time(datetime.utcnow())
