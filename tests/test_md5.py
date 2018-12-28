#!/usr/bin/env python3

import pytest

from bella import md5


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
