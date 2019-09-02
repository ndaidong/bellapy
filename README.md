# bellapy
BellaPy - A useful helper for any python program

[![PyPI version](https://badge.fury.io/py/bella.svg)](https://badge.fury.io/py/bella)
[![Build Status](https://travis-ci.org/ndaidong/bellapy.svg?branch=master)](https://travis-ci.org/ndaidong/bellapy)


## Contents

* [Setup](#setup)
* [APIs](#apis)
* [Dev & Test](#dev-test)
* [License](#license)


## Setup

```bash
pip install bella
```


# APIs

- genid(leng, prefix)

Return a random string


```python
from bella import genid

print(genid())  # --> akrqHX7eQyT3neF6
print(genid(5))  # --> xzxNK
print(genid(10, 'id_'))  # --> id_j0fpXAZ
```


### Hashing



```python
from bella import md5, md160
```


- `md5(text)`

Return md5 hashed string


```python
md5('hello')  # --> 5d41402abc4b2a76b9719d911017c592
```


- `md160(text)`

Return md160 hashed string


```python
md160('hello')  # --> 108f07b8382412612c048d07d13f814118445acd
```


- `sha256(password, salt, dkpower)`

Return sha256 hashed string


```python
sha256('1234', 'v23')
# --> 457b01a0f6169725

# dkpower relates to length of output, default is 3
# output length = 2 ** (dkpower + 1)
# for example with dkpower = 4 --> output length = 2 ** 5 = 32
sha256('1234', 'v23', dkpower=4)
# --> 457b01a0f61697250083c598f7b8a8fd
```


### Slugify


```python
from bella import slugify

slugify('BellaPy - A useful helper for any python program')
# => bellapy-a-useful-helper-for-any-python-program

slugify('Ngày hội “đám mây” của Amazon')
# => ngay-hoi-dam-may-cua-amazon
```

### Plurialize

Return plural form of a noun:

```python
from bella import plurialize

plurialize('leaf', 1)  # => leaf
plurialize('leaf', 2)  # => leaves

```

### Detection

- `is_int(value)`

Return True if value is integer

- `is_float(value)`

Return True if value is float

- `is_num(value)`

Return True if value is number

- `is_bool(value)`

Return True if value is boolean

- `is_str(value)`

Return True if value is string

- `is_list(value)`

Return True if value is list

- `is_dict(value)`

Return True if value is dict


### Date & time


- `get_time()`

Return current timestamp (passed mili seconds since 00:00:00 1/1/1970)

- `format_time(time, pattern)`

Return formated datetime string of `time` by specific `pattern`


- `get_local_time()`

Return current datetime of local system

- `get_utc_time()`

Return current UCT datetime


### Filesystem


```python
from bella import fs
```

- `fs.copy(source, dest)`

Copy file or folder `source` into `dest`, then return result as Boolean


- `fs.remove(path)`

Remove given file or folder, then return result as Boolean


- `fs.write_json_to_file(file_path, json_data)`

Write JSON data into given file path


- `fs.read_json_from_file(file_path)`

Return JSON data from given file



### Utils


- `throttle` decorator

```python
from bella import throttle


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
```

- `timing` decorator

```python
from bella import timing, fs

@timing('save_item')
def save_item(data):
    fs.write_json_to_file('./cache.json', data)


save_item(dict(name='Alice'))
# output:
# Timing for save_item: 0.00134 s
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
