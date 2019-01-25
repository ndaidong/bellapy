#!/usr/bin/env python3

from time import time
from datetime import datetime
from dateutil.relativedelta import relativedelta


DEFAULT_PATTERN = '%a, %b %d, %Y %H:%M:%S'


def get_time(ms=False):
    if ms:
        return time()
    return int(time())


def format_time(d=datetime.now(), pattern=DEFAULT_PATTERN):
    return d.strftime(pattern)


def get_local_time():
    return format_time(datetime.now())


def get_utc_time():
    return format_time(datetime.utcnow())


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
