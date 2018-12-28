#!/usr/bin/env python3

from time import time
from datetime import datetime


DEFAULT_PATTERN = '%a, %b %d, %Y %H:%M:%S %p'


def get_time(ms=False):
    if ms:
        return time()
    return int(time())


def format_time(d=datetime.now(), pattern=DEFAULT_PATTERN):
    return d.strftime(pattern)


def get_local_time():
    now = datetime.now()
    return format_time(now)


def get_utc_time():
    now = datetime.utcnow()
    return format_time(now)


def get_times_distance(t0, t1):
    start, stop = t0, t1
    if t0 > t1:
        stop, start = t0, t1
    t_diff = relativedelta(stop, start)
    return '{d}d {h}h {m}m {s}s'.format(
        d=t_diff.days,
        h=t_diff.hours,
        m=t_diff.minutes,
        s=t_diff.seconds
    )
