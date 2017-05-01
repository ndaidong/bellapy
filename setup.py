from setuptools import setup

setup(
  name = 'bella',
  version = '0.0.1',
  packages = ['bella'],
  description = 'Utils for Python',

  url = 'https://github.com/ndaidong/bellapy',

  author = '@ndaidong',
  author_email = 'ndaidong@protonmail.com',

  license = 'MIT',

  classifiers = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development :: Libraries',
    'Topic :: Utilities'
  ],

  keywords = 'detection, manipulation, stabilize, immutable, datetime, utils, helpers',

  install_requires = [],

  extras_require = {
    'dev': ['check-manifest'],
    'test': ['coverage'],
  },
  package_data = {},
  data_files = [],

  entry_points = {
    'console_scripts': [
      'bella=bella',
    ],
  },
)
