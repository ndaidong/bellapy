#!/usr/bin/env python3

import pytest

from bella import pluralize


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
