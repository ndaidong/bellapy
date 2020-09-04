#!/usr/bin/env python3

import pytest

from bella import pluralize, slugify, remove_tags, truncate


def test_pluralize():
    words = ['car', 'person', 'new', 'reply', 'box']
    expects = ['cars', 'people', 'news', 'replies', 'boxes']
    i = 0
    while i < len(words):
        word = words[i]
        expect = expects[i]
        plword = pluralize(word, 10)
        if plword != expect:
            pytest.fail('pluralize("{}") must return "{}"'.format(
                word, expect
            ))
        i += 1


def test_slugify():
    samples = [
        dict(
            value='BellaPy - A useful helper for any python program',
            expect='bellapy-a-useful-helper-for-any-python-program'
        ),
        dict(
            value='Ngày hội “đám mây” của Amazon',
            expect='ngay-hoi-dam-may-cua-amazon'
        )
    ]
    for sample in samples:
        value = sample['value']
        actual = slugify(value)
        expect = sample['expect']
        if actual != expect:
            pytest.fail('slugify(`{}`) must return `{}`, not `{}`'.format(
                value, expect, actual
            ))


def test_remove_tags():
    samples = [
        dict(
            value='A useful <b>helper</b> for any <code>python</code> program',
            expect='A useful helper for any python program'
        ),
        dict(
            value='<title>Ngày hội “đám mây” của Amazon</title>',
            expect='Ngày hội “đám mây” của Amazon'
        )
    ]
    for sample in samples:
        value = sample['value']
        actual = remove_tags(value)
        expect = sample['expect']
        if actual != expect:
            pytest.fail('remove_tags(`{}`) must return `{}`, not `{}`'.format(
                value, expect, actual
            ))


def test_truncate():
    samples = [
        dict(
            value='A useful helper for any python program',
            expect='A useful helper for any python program'
        ),
        dict(
            value=' '.join([
                'This document is designed to help system administrators',
                'and DevOps focused organisations to understand bare metal',
                'server provisioning, understand its value proposition, and',
                'learn about how leading companies are using server',
                'provisioning solutions within their hyperscale environments.'
            ]),
            expect='This document is designed to help system administrators...'
        )
    ]
    for sample in samples:
        value = sample['value']
        actual = truncate(value, 50)
        expect = sample['expect']
        if actual != expect:
            pytest.fail('truncate(`{}`) must return `{}`, not `{}`'.format(
                value, expect, actual
            ))
