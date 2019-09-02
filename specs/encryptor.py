#!/usr/bin/env python3

import pytest

from bella import genid, md5, md160, sha256


def test_genid():
    id1 = genid()
    id2 = genid(16)
    id3 = genid(32)
    id4 = genid(40, '__::')
    if not isinstance(id1, str):
        pytest.fail('Generated ID must be string')
    if len(id2) != 16:
        pytest.fail('genid(16) must return 16 characters')
    if len(id3) != 32:
        pytest.fail('genid(32) must return 32 characters')
    if len(id4) != 40:
        pytest.fail('genid(40) must return 40 characters')
    if not id4.startswith('__::', 0):
        pytest.fail('genid(40, "__::") must start with "__::"')


def test_md5():
    samples = [
        dict(
            key='hello',
            value='5d41402abc4b2a76b9719d911017c592'
        ),
        dict(
            key=1996,
            value='6351bf9dce654515bf1ddbd6426dfa97'
        ),
        dict(
            key='',
            value=''
        ),
        dict(
            key=None,
            value=''
        )
    ]
    for sample in samples:
        key = sample.get('key')
        expect = sample.get('value')
        actual = md5(key)
        if expect != actual:
            pytest.fail(
                'md5("{}") must be "{}", not "{}"'.format(
                    key, expect, actual
                )
            )


def test_md160():
    samples = [
        dict(
            key='hello',
            value='108f07b8382412612c048d07d13f814118445acd'
        ),
        dict(
            key=1996,
            value='c966d193ce1337096d29c28ae183cc1b317fa370'
        ),
        dict(
            key='',
            value=''
        ),
        dict(
            key=None,
            value=''
        )
    ]
    for sample in samples:
        key = sample.get('key')
        expect = sample.get('value')
        actual = md160(key)
        if expect != actual:
            pytest.fail(
                'md160("{}") must be "{}", not "{}"'.format(
                    key, expect, actual
                )
            )


def test_sha256():
    password = '1234'
    salt = 'v23'
    expect = '457b01a0f6169725'
    actual = sha256(password, salt)
    if expect != actual:
        pytest.fail(
            'sha256("{}", "{}") must be "{}", not "{}"'.format(
                password, salt, expect, actual
            )
        )
    # change dkpower
    dkpower = 4
    expect = '457b01a0f61697250083c598f7b8a8fd'
    actual = sha256(password, salt, dkpower=dkpower)
    if expect != actual:
        pytest.fail(
            'sha256("{}", "{}", dkpower={}) must be "{}", not "{}"'.format(
                password, salt, dkpower, expect, actual
            )
        )
