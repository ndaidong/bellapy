# bellapy
BellaPy - A useful helper for any python program

[![PyPI version](https://badge.fury.io/py/bella.svg)](https://badge.fury.io/py/bella)
[![Build Status](https://travis-ci.org/ndaidong/bellapy.svg?branch=master)](https://travis-ci.org/ndaidong/bellapy)
[![Coverage Status](https://coveralls.io/repos/github/ndaidong/bellapy/badge.svg?branch=master)](https://coveralls.io/github/ndaidong/bellapy?branch=master)


## Contents

* [Setup](#setup)
* [APIs](#apis)
* [Dev & Test](#dev--test)
* [License](#license)


## Setup

```bash
pip install bella

# or build from source
git clone https://github.com/ndaidong/bellapy.git
cd bellapy
python3 setup.py install
```

## Usage

```py
from bella import genid, md5

genid()  # --> akrqHX7eQyT3neF6
genid(5)  # --> xzxNK
md5('hello')  # --> 5d41402abc4b2a76b9719d911017c592
```


# APIs

### Datatype detection

-  is_int(val: Any)
-  is_float(val: Any)
-  is_num(val: Any)
-  is_str(val: Any)
-  is_bool(val: Any)
-  is_list(val: Any)
-  is_dict(val: Any)
-  is_valid_url(val: Any)


### Encryption

```python
md5(text: str)
md160(text: str)
sha256(text: str, salt: str, dkpower: int = 3, iterations: int = 50000)
```

Examples:

```python
md5('hello')  # --> 5d41402abc4b2a76b9719d911017c592
md160('hello')  # --> 108f07b8382412612c048d07d13f814118445acd
sha256('1234', 'v23')  # --> 457b01a0f6169725

# dkpower relates to length of output, default is 3
# output length = 2 ** (dkpower + 1)
# for example with dkpower = 4 --> output length = 2 ** 5 = 32
sha256('1234', 'v23', dkpower=4) # --> 457b01a0f61697250083c598f7b8a8fd
```


### Date & time


```python
PY_DATE_PATTERN  # '%Y-%m-%d %H:%M:%S %z'
MY_DATE_PATTERN  # '%a, %b %d, %Y %H:%M:%S'

get_time()
format_time(datetime, pattern)
get_local_time()
get_utc_time()
```

Examples

```python
from bella import PY_DATE_PATTERN, format_time, get_time

now = get_time()
date_str = format_time(now, PY_DATE_PATTERN)
print(date_str)
```

### Filesystem


```python
from bella import fs

fs.exists(file_path: str)
fs.isdir(file_path: str)
fs.isfile(file_path: str)

# Get list of child files/folders by specific glob pattern
fs.get_files(pattern)

# Copy file or folder `source` into `dest`:
fs.copy(source, dest)

# Remove file or folder
fs.remove(path)
```


### Utils

```python
genid(count: int = 16,  prefix: str = '') # return a random string
slugify(text: str) # create slug from a string
strip_accents(text: str) # remove accents string
remove_tags(text: str) # remove HTML tags from a string
truncate(text: str, maxlen: int) # cut a long string to shorter one
plurialize(word: str = None, count: int = 1) # return plural format of word
byte_to_text(bytesize: int, precision: int = 2)

write_json_to_file(file_path: str = '', data: dict = {})
read_json_from_file(file_path: str = '')
jprint(data: Any, sorting=True, identation=2)

throttle(seconds: int) # decorator, make a function throttling
timing(name: str) # decorator, measure time to execute an expression

has_installed(package) # check if a python package is installed

curry(func) # make `func` become a curry function
compose(functions) # performs right-to-left function composition
pipe(functions) # performs left-to-right function composition
```

Examples:

```python
print(genid())  # --> akrqHX7eQyT3neF6
print(genid(5))  # --> xzxNK
print(genid(10, 'id_'))  # --> id_j0fpXAZ

slugify('BellaPy - A useful helper for any python program')
# --> bellapy-a-useful-helper-for-any-python-program
slugify('Ngày hội “đám mây” của Amazon')
# --> ngay-hoi-dam-may-cua-amazon

plurialize('leaf', 1)  # => leaf
plurialize('leaf', 2)  # => leaves

@throttle(5)
def fn(a):
    print('No call multi times within 5 seconds')
    print(a)

fn(1)
fn(2)
fn(3)
fn(4)
fn(5)
fn(6)
fn(7)

@timing('save_item')
def save_item(data):
    write_json_to_file('./cache.json', data)

save_item(dict(name='Alice'))
# => Timing for save_item: 0.00134 s
```


# Dev & Test

```bash
git clone https://github.com/ndaidong/bellapy.git
cd bellapy
python3 -m venv venv
source venv/bin/activate
(venv) pip install -r requirements.txt
(venv) ./test.sh
```


# License

The MIT License (MIT)
