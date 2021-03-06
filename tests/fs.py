#!/usr/bin/env python3

from os import system

import pytest

from bella import fs


TMPDIR = 'ptester'


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


def test_copy_files():
    system(f'mkdir -p {TMPDIR}/source')
    system(f'mkdir -p {TMPDIR}/dest')
    given = ['a.ext', 'b.ext', 'c.ext']
    for afile in given:
        system(f'touch {TMPDIR}/source/{afile}')
        fs.copy(f'{TMPDIR}/source/{afile}', f'{TMPDIR}/dest')
    for afile in given:
        fpath = f'{TMPDIR}/dest/{afile}'
        if not fs.exists(fpath):
            pytest.fail(f'"{fpath}" must be existed')


def test_remove_files():
    given = ['a.ext', 'b.ext', 'c.ext']
    for afile in given:
        fpath = f'{TMPDIR}/dest/{afile}'
        fs.remove(fpath)
        if fs.exists(fpath):
            pytest.fail(f'"{fpath}" must be removed')
