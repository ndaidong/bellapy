#!/usr/bin/env python3

import pytest

from bella import byte_to_text, curry, compose, pipe, \
    write_json_to_file, read_json_from_file, fs, is_dict


TMPDIR = 'ptester'


def test_byte_to_text():
    samples = [
        dict(
            value=5,
            expect='5 bytes'
        ),
        dict(
            value=3000,
            expect='2.93 K'
        ),
        dict(
            value=50 * 1024 * 10e4,
            expect='4.77 G'
        ),
        dict(
            value=50 * 1024 * 10e6,
            expect='476.84 G'
        ),
        dict(
            value=50 * 1024 * 10e8,
            expect='46.57 TB'
        )
    ]
    for sample in samples:
        value = sample['value']
        actual = byte_to_text(value)
        expect = sample['expect']
        if actual != expect:
            pytest.fail('byte_to_text(`{}`) must return `{}`, not `{}`'.format(
                value, expect, actual
            ))


def test_curry():

    def normal_sum(a, b, c):
        return a + b + c

    curried_sum = curry(normal_sum)

    samples = [
        dict(
            fn_str='curried_sum(3, 2, 1)',
            actual=curried_sum(3, 2, 1),
            expect=6
        ),
        dict(
            fn_str='curried_sum(3, 2)(1)',
            actual=curried_sum(3, 2)(1),
            expect=6
        ),
        dict(
            fn_str='curried_sum(3)(2, 1)',
            actual=curried_sum(3)(2, 1),
            expect=6
        ),
        dict(
            fn_str='curried_sum(3)(2)(1)',
            actual=curried_sum(3)(2)(1),
            expect=6
        )
    ]
    for sample in samples:
        fn_str = sample['fn_str']
        actual = sample['actual']
        expect = sample['expect']
        if actual != expect:
            pytest.fail('{} must return `{}`, not `{}`'.format(
                fn_str, expect, actual
            ))


def test_compose():

    def add1(x):
        return x + 1

    def mult2(x):
        return x * 2

    add1AndMult2 = compose(add1, mult2)
    value = 3
    actual = add1AndMult2(value)
    expect = 7
    if actual != expect:
        pytest.fail('add1AndMult2(`{}`) must return `{}`, not `{}`'.format(
            value, expect, actual
        ))


def test_pipe():

    def add1(x):
        return x + 1

    def mult2(x):
        return x * 2

    add1AndMult2 = pipe(add1, mult2)
    value = 3
    actual = add1AndMult2(value)
    expect = 8
    if actual != expect:
        pytest.fail('add1AndMult2(`{}`) must return `{}`, not `{}`'.format(
            value, expect, actual
        ))


def test_write_json_to_file():
    fpath = f'{TMPDIR}/test-json'
    data = {'name': 'bella'}
    write_json_to_file(fpath, data)
    if not fs.exists(fpath):
        pytest.fail(f'"{fpath}" must be created')


def test_read_json_from_file():
    fpath = f'{TMPDIR}/test-json'
    data = read_json_from_file(fpath)
    if not is_dict(data):
        pytest.fail('JSON data must be dict')
