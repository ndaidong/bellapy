#!/usr/bin/env python3

import string
import hashlib

from random import shuffle, choice


def genid(count=16, prefix=''):
    alphadigits = string.ascii_letters + string.digits
    alphadigits_list = list(alphadigits)
    shuffle(alphadigits_list)
    alphadigits = ''.join(alphadigits_list)
    leng = count - len(prefix)
    if leng < 0:
        return prefix
    return prefix + ''.join([choice(alphadigits) for n in range(leng)])


def _xhash(txt='', algorithm='md5'):
    if not txt:
        return ''
    if algorithm == 'ripemd160':
        m = hashlib.new('ripemd160')
    else:
        m = hashlib.md5()
    m.update(str(txt).encode('utf-8'))
    return m.hexdigest()


def md5(txt=''):
    return _xhash(txt, md5)


def md160(txt=''):
    return _xhash(txt, 'ripemd160')
