#!/usr/bin/env python3

import pytest

from bella import md160


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
