#!/usr/bin/env python3

# flake8: noqa

from specs.detector import *
from specs.encryptor import test_genid, test_md5, test_md160, test_sha256
from specs.text_manipulation import test_pluralize, \
    test_slugify, test_remove_tags, test_truncate
from specs.utils import test_byte_to_text, test_compose, \
    test_pipe, test_curry
from specs.fs import *
