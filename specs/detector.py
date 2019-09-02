#!/usr/bin/env python3

import pytest

from bella import is_int, is_float, is_num, is_str, \
    is_bool, is_list, is_dict, is_valid_url


def test_is_int():
    samples = [
        dict(
            value=1,
            expect=True
        ),
        dict(
            value=-21,
            expect=True
        ),
        dict(
            value=99,
            expect=True
        ),
        dict(
            value=2.5,
            expect=False
        ),
        dict(
            value='123',
            expect=False
        ),
        dict(
            value=None,
            expect=False
        )
    ]
    for sample in samples:
        value = sample.get('value')
        expect = sample.get('expect')
        actual = is_int(value)
        if expect != actual:
            pytest.fail(
                'is_int({}) must be {}, not {}'.format(
                    value, expect, actual
                )
            )


def test_is_float():
    samples = [
        dict(
            value=1,
            expect=False
        ),
        dict(
            value=99,
            expect=False
        ),
        dict(
            value=-2.5,
            expect=True
        ),
        dict(
            value=0.5,
            expect=True
        ),
        dict(
            value=2.5,
            expect=True
        ),
        dict(
            value='12.3',
            expect=False
        ),
        dict(
            value=None,
            expect=False
        )
    ]
    for sample in samples:
        value = sample.get('value')
        expect = sample.get('expect')
        actual = is_float(value)
        if expect != actual:
            pytest.fail(
                'is_float({}) must be {}, not {}'.format(
                    value, expect, actual
                )
            )


def test_is_num():
    samples = [
        dict(
            value=1,
            expect=True
        ),
        dict(
            value=99,
            expect=True
        ),
        dict(
            value=-2.5,
            expect=True
        ),
        dict(
            value=0.5,
            expect=True
        ),
        dict(
            value=2.5,
            expect=True
        ),
        dict(
            value='12.3',
            expect=False
        ),
        dict(
            value=None,
            expect=False
        )
    ]
    for sample in samples:
        value = sample.get('value')
        expect = sample.get('expect')
        actual = is_num(value)
        if expect != actual:
            pytest.fail(
                'is_num({}) must be {}, not {}'.format(
                    value, expect, actual
                )
            )


def test_is_str():
    samples = [
        dict(
            value=b'abc',
            expect=False
        ),
        dict(
            value='abc',
            expect=True
        ),
        dict(
            value=1,
            expect=False
        ),
        dict(
            value=99,
            expect=False
        ),
        dict(
            value=-2.5,
            expect=False
        ),
        dict(
            value=0.5,
            expect=False
        ),
        dict(
            value=2.5,
            expect=False
        ),
        dict(
            value='12.3',
            expect=True
        ),
        dict(
            value='',
            expect=True
        ),
        dict(
            value=None,
            expect=False
        )
    ]
    for sample in samples:
        value = sample.get('value')
        expect = sample.get('expect')
        actual = is_str(value)
        if expect != actual:
            pytest.fail(
                'is_str({}) must be {}, not {}'.format(
                    value, expect, actual
                )
            )


def test_is_bool():
    samples = [
        dict(
            value=b'abc',
            expect=False
        ),
        dict(
            value='abc',
            expect=False
        ),
        dict(
            value=1,
            expect=False
        ),
        dict(
            value=99,
            expect=False
        ),
        dict(
            value=-2.5,
            expect=False
        ),
        dict(
            value=False,
            expect=True
        ),
        dict(
            value=True,
            expect=True
        ),
        dict(
            value=0,
            expect=False
        ),
        dict(
            value=1,
            expect=False
        ),
        dict(
            value='',
            expect=False
        ),
        dict(
            value=None,
            expect=False
        )
    ]
    for sample in samples:
        value = sample.get('value')
        expect = sample.get('expect')
        actual = is_bool(value)
        if expect != actual:
            pytest.fail(
                'is_bool({}) must be {}, not {}'.format(
                    value, expect, actual
                )
            )


def test_is_list():
    samples = [
        dict(
            value=[],
            expect=True
        ),
        dict(
            value=[1, 2, 3],
            expect=True
        ),
        dict(
            value=list(('a', 3, 2)),
            expect=True
        ),
        dict(
            value=2.5,
            expect=False
        ),
        dict(
            value='123',
            expect=False
        ),
        dict(
            value=None,
            expect=False
        )
    ]
    for sample in samples:
        value = sample.get('value')
        expect = sample.get('expect')
        actual = is_list(value)
        if expect != actual:
            pytest.fail(
                'is_list({}) must be {}, not {}'.format(
                    value, expect, actual
                )
            )


def test_is_dict():
    samples = [
        dict(
            value=[],
            expect=False
        ),
        dict(
            value=[1, 2, 3],
            expect=False
        ),
        dict(
            value=('a', 3, 2),
            expect=False
        ),
        dict(
            value=dict(),
            expect=True
        ),
        dict(
            value=dict(name='Alice'),
            expect=True
        ),
        dict(
            value={},
            expect=True
        ),
        dict(
            value={'name': 'Alice'},
            expect=True
        ),
        dict(
            value=2.5,
            expect=False
        ),
        dict(
            value='123',
            expect=False
        ),
        dict(
            value=None,
            expect=False
        )
    ]
    for sample in samples:
        value = sample.get('value')
        expect = sample.get('expect')
        actual = is_dict(value)
        if expect != actual:
            pytest.fail(
                'is_dict({}) must be {}, not {}'.format(
                    value, expect, actual
                )
            )


def test_is_valid_url():
    samples = [
        dict(
            value=[],
            expect=False
        ),
        dict(
            value=[1, 2, 3],
            expect=False
        ),
        dict(
            value=('a', 3, 2),
            expect=False
        ),
        dict(
            value=dict(),
            expect=False
        ),
        dict(
            value=dict(name='Alice'),
            expect=False
        ),
        dict(
            value={},
            expect=False
        ),
        dict(
            value={'name': 'Alice'},
            expect=False
        ),
        dict(
            value=2.5,
            expect=False
        ),
        dict(
            value='123',
            expect=False
        ),
        dict(
            value=None,
            expect=False
        ),
        dict(
            value='http//abc.com',
            expect=False
        ),
        dict(
            value='http://abc.com',
            expect=True
        ),
        dict(
            value='http://abc.com/path?arg=1',
            expect=True
        ),
        dict(
            value='https://abc.com',
            expect=True
        )
    ]
    for sample in samples:
        value = sample.get('value')
        expect = sample.get('expect')
        actual = is_valid_url(value)
        if expect != actual:
            pytest.fail(
                'is_valid_url({}) must be {}, not {}'.format(
                    value, expect, actual
                )
            )
