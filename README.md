# bellapy
BellaPy - A useful helper for any python program


[![Build Status](https://travis-ci.org/ndaidong/bellapy.svg?branch=master)](https://travis-ci.org/ndaidong/bellapy)
[![Coverage Status](https://coveralls.io/repos/github/ndaidong/bellapy/badge.svg?branch=master)](https://coveralls.io/github/ndaidong/bellapy?branch=master)


# Contents

* [Setup](#setup)
* [APIs](#apis)
* [Test](#test)
* [License](#license)


## Setup

  ```
  pip install bella

  // or local install
  pip install -e git+https://github.com/ndaidong/bellapy.git
  ```

# APIs

- createId(int leng = 16)

Return a random string

```
from bella import createId

print(createId())
print(createId(32))
print(createId(40))
```


// coming soon

# Test

```
git clone https://github.com/ndaidong/bellapy.git
cd bellapy
pip install -e .
./test
```


# License

The MIT License (MIT)