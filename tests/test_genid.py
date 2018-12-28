#!/usr/bin/env python3

import pytest

from bella import genid


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
