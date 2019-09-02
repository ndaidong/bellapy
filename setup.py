#!/usr/bin/env python3

from setuptools import setup


PACKAGE = 'bella'
VERSION = open(PACKAGE + '/VERSION').read().strip()
README = open('README.md').read().strip()


setup(
    name=PACKAGE,
    version=VERSION,
    packages=[PACKAGE],

    description="BellaPy - A useful helper for any python program",
    long_description=README,
    long_description_content_type="text/markdown",

    url='https://github.com/ndaidong/bellapy',

    author='@ndaidong',
    author_email='ndaidong@gmail.com',

    license='MIT',

    classifiers=[
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities'
    ],

    keywords='detection, manipulation, datetime, utils, helpers',

    install_requires=[],

    extras_require={
        'test': ['pycodestyle', 'safety', 'pytest'],
    },
    include_package_data=True,

    zip_safe=False,

    entry_points={
        'console_scripts': [
            'bella=bella:init'
        ]
    }
)
