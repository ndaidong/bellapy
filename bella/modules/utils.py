#!/usr/bin/env python3

import time
import json
from typing import Any
from functools import reduce
from urllib.parse import urlparse
from importlib.util import find_spec
from json import dumps, load

from .logger import log
from .fs import exists


def throttle(seconds: int):
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


def timing(name: str):
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


def write_json_to_file(file_path: str = '', data: dict = {}):
    try:
        jstr = dumps(data, indent=2, sort_keys=True, ensure_ascii=False)
        with open(file_path, 'w') as write_file:
            write_file.write(jstr)
            write_file.flush()
        return True
    except Exception as err:
        log('write_json_to_file', file_path, err)
        pass
    return False


def read_json_from_file(file_path: str = ''):
    try:
        if exists(file_path):
            with open(file_path, 'r') as read_file:
                return load(read_file)
    except Exception as err:
        log('read_json_from_file', file_path, err)
        pass
    return {}


def jprint(data: Any, sorting=True, identation=2):
    try:
        if type(data) is str:
            data = json.loads(data)
        return print(json.dumps(
            data, sort_keys=sorting, indent=identation
        ))
    except Exception as err:
        log('jprint', err)
        pass
    return print(data)


def byte_to_text(bytesize, precision=2):
    abbrevs = (
        (1 << 50, 'PB'),
        (1 << 40, 'TB'),
        (1 << 30, 'G'),
        (1 << 20, 'M'),
        (1 << 10, 'K'),
        (1, 'bytes')
    )
    if bytesize == 1:
        return '1 byte'
    for factor, suffix in abbrevs:
        if bytesize >= factor:
            break
    if factor == 1:
        precision = 0
    result = bytesize / float(factor)
    if result <= 0:
        return 0
    return '%.*f %s' % (precision, result, suffix)


def get_base_url(url):
    try:
        result = urlparse(url)
        return '://'.join([result.scheme, result.netloc])
    except Exception as err:
        log('get_base_url', url)
        pass
    return url


def has_installed(pkg):
    return find_spec(pkg) is not None


def compose(*fns):
    return reduce(
        lambda f, g: lambda x: f(g(x)),
        fns,
        lambda x: x
    )


def pipe(*fns):
    return reduce(
        lambda f, g: lambda x: g(f(x)),
        fns,
        lambda x: x
    )


def curry(func):
    f_args = []
    f_kwargs = {}

    def f(*args, **kwargs):
        nonlocal f_args, f_kwargs
        if args or kwargs:
            f_args += args
            f_kwargs.update(kwargs)
            return f
        else:
            return func(*f_args, *f_kwargs)
    return f
