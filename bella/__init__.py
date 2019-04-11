#!/usr/bin/env python3

import os
from argparse import ArgumentParser

from .modules import fs
from .modules import hw

from .modules.text import genid, md5, md160

from .modules.utime import get_time, format_time, \
    get_local_time, get_utc_time, get_times_distance

from .modules.detector import is_int, is_num, is_float, is_str, \
    is_list, is_dict, is_valid_url

from .modules.utils import throttle, timing, jprint


def version():
    f = os.path.dirname(os.path.realpath(__file__))
    return open(f + '/VERSION').read().strip()


def init():
    parser = ArgumentParser()
    parser.add_argument(
        '-v',
        '--version',
        default='',
        action='store_true',
        help='check version'
    )
    args = parser.parse_args()
    ver = args.version
    if ver:
        return print('bella v{}'.format(version()))


if __name__ == '__main__':
    init()
