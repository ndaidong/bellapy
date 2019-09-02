#!/usr/bin/env python3

import os

ENV = os.getenv('ENV', 'prod')


def log(*args):
    if ENV == 'dev':
        print(*args)
