#!/usr/bin/env python3

from os import system

import pytest

from bella import fs


TMPDIR = 'storage'


def test_exists():
    if not fs.exists(TMPDIR):
        pytest.fail(f'"{TMPDIR}" must be existed')


def test_isdir():
    if not fs.isdir(TMPDIR):
        pytest.fail(f'"{TMPDIR}" must be a directory')


def test_isfile():
    a_file = f'{TMPDIR}/a_file.txt'
    system(f'touch {a_file}')
    if not fs.isfile(a_file):
        pytest.fail(f'"{a_file}" must be a file')


def test_get_files():
    given = ['a.ext', 'b.ext', 'c.ext']
    for afile in given:
        system(f'touch {TMPDIR}/{afile}')
    take = fs.get_files('*.ext')
    if not all([a in given for a in take]):
        pytest.fail('get_files must return all .ext files')
