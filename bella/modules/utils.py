#!/usr/bin/env python3

import time
import json


def throttle(s):
    def decorate(f):
        t = None

        def wrapped(*args, **kwargs):
            nonlocal t
            t_ = time.time()
            if t is None or t_ - t >= s:
                result = f(*args, **kwargs)
                t = time.time()
                return result
        return wrapped
    return decorate


def timing(name):
    def caller(f):
        def wrap(*args):
            start = time.time()
            ret = f(*args)
            end = time.time()
            ms = end - start
            print('Timing for `{}`: {}'.format(
                name,
                str(round(ms, 2)) + ' s'
            ))
            return ret
        return wrap
    return caller


def jprint(data, sorting=True, identation=2):
    try:
        if type(data) is str:
            data = json.loads(data)
        return print(json.dumps(
            data, sort_keys=sorting, indent=identation
        ))
    except Exception as err:
        print(err)
        pass
    return print(data)


def to_str(v):
    try:
        return str(v)
    except Exception as err:
        print(err)
        pass
    return v


def to_int(v):
    try:
        return int(v)
    except Exception as err:
        print(err)
        pass
    return v
