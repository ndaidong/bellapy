#!/usr/bin/env python3

from .modules import fs

from .modules.detector import is_int, is_num, is_float, is_str, \
    is_bool, is_list, is_dict, is_valid_url

from .modules.text import genid, slugify, remove_tags, pluralize, \
    md5, md160, sha256

from .modules.utime import get_time, get_local_time, get_utc_time, \
    format_time, PY_DATE_PATTERN, MY_DATE_PATTERN

from .modules.utils import throttle, timing, jprint, \
    write_json_to_file, read_json_from_file, \
    byte_to_text, get_base_url, has_installed, \
    compose, pipe, curry


def version():
    f = os.path.dirname(os.path.realpath(__file__))
    return open(f + '/VERSION').read().strip()
