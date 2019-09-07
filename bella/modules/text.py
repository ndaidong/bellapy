#!/usr/bin/env python3

import re
import string
import hashlib
import binascii

from random import shuffle, choice

from .logger import log

TAG_RE = re.compile(r'<[^>]+>')


def genid(count: int = 16, prefix: str = ''):
    alphadigits = string.ascii_letters + string.digits
    alphadigits_list = list(alphadigits)
    shuffle(alphadigits_list)
    alphadigits = ''.join(alphadigits_list)
    leng = count - len(prefix)
    if leng < 0:
        return prefix
    return prefix + ''.join([choice(alphadigits) for n in range(leng)])


def get_char_map():
    char_map = {
        'a': 'á|à|ả|ã|ạ|ă|ắ|ặ|ằ|ẳ|ẵ|â|ấ|ầ|ẩ|ẫ|ậ|ä',
        'A': 'Á|À|Ả|Ã|Ạ|Ă|Ắ|Ặ|Ằ|Ẳ|Ẵ|Â|Ấ|Ầ|Ẩ|Ẫ|Ậ|Ä',
        'c': 'ç',
        'C': 'Ç',
        'd': 'đ',
        'D': 'Đ',
        'e': 'é|è|ẻ|ẽ|ẹ|ê|ế|ề|ể|ễ|ệ|ë',
        'E': 'É|È|Ẻ|Ẽ|Ẹ|Ê|Ế|Ề|Ể|Ễ|Ệ|Ë',
        'i': 'í|ì|ỉ|ĩ|ị|ï|î',
        'I': 'Í|Ì|Ỉ|Ĩ|Ị|Ï|Î',
        'o': 'ó|ò|ỏ|õ|ọ|ô|ố|ồ|ổ|ỗ|ộ|ơ|ớ|ờ|ở|ỡ|ợ|ö',
        'O': 'Ó|Ò|Ỏ|Õ|Ọ|Ô|Ố|Ồ|Ổ|Ô|Ộ|Ơ|Ớ|Ờ|Ở|Ỡ|Ợ|Ö',
        'u': 'ú|ù|ủ|ũ|ụ|ư|ứ|ừ|ử|ữ|ự|û',
        'U': 'Ú|Ù|Ủ|Ũ|Ụ|Ư|Ứ|Ừ|Ử|Ữ|Ự|Û',
        'y': 'ý|ỳ|ỷ|ỹ|ỵ',
        'Y': 'Ý|Ỳ|Ỷ|Ỹ|Ỵ'
    }
    xmap = {}
    for k in char_map:
        arr = char_map[k].split('|')
        for key in arr:
            xmap[key] = k
    return xmap


CHARS_MAP = get_char_map()


def strip_accents(text: str):
    def check_and_replace(c):
        if c in CHARS_MAP:
            return CHARS_MAP[c]
        return c

    mod = [check_and_replace(a) for a in text]
    return ''.join(mod)


def slugify(text: str):
    text = strip_accents(text).lower()
    return re.sub(r'[\W_]+', '-', text)


def remove_tags(html: str):
    return TAG_RE.sub('', html)


def truncate(text: str, maxlen: int = 128):
    if len(text) <= maxlen + 5:
        return text
    words = text.split(' ')
    selected = []
    extracted_size = 0
    for word in words:
        word = word.strip()
        selected.append(word)
        extracted_size += len(word) + 1
        if extracted_size > maxlen:
            break
    return ' '.join(selected) + '...'


def _xhash(txt='', algorithm='md5'):
    if algorithm == 'ripemd160':
        m = hashlib.new('ripemd160')
    else:
        m = hashlib.md5()
    m.update(str(txt).encode('utf-8'))
    return m.hexdigest()


def md5(txt: str):
    if not txt:
        return ''
    return _xhash(str(txt), md5)


def md160(txt: str):
    if not txt:
        return ''
    return _xhash(str(txt), 'ripemd160')


def sha256(txt: str, salt: str, iterations: int = 50000, dkpower: int = 3):
    dk = hashlib.pbkdf2_hmac(
        'sha256',
        str(txt).encode('utf8'),
        'salt'.encode('utf8'),
        iterations,
        2 ** dkpower
    )
    return binascii.hexlify(dk).decode('ascii')


# pluralize(word, count):
# return: plural form of a countable noun depending on its quantity
# function customized from the following script:
# http://code.activestate.com/recipes/577781-pluralize-word-convert-singular-word-to-its-plural/

ABERRANT_PLURAL_MAP = {
    'antenna': 'algae',
    'appendix': 'appendices',
    'baggage': 'baggage',
    'barracks': 'barracks',
    'corpus': 'corpora',
    'child': 'children',
    'deer': 'deer',
    'focus': 'foci',
    'fungus': 'fungi',
    'furniture': 'furniture',
    'genus': 'genera',
    'goose': 'geese',
    'index': 'indices',
    'information': 'information',
    'larva': 'larvae',
    'luggage': 'luggage',
    'man': 'men',
    'mouse': 'mice',
    'news': 'news',
    'nucleus': 'nuclei',
    'person': 'people',
    'syllabus': 'syllabi',
    'vertebra': 'vertebrae',
    'woman': 'women',
}

VOWELS = set('aeiou')

NORMAL_O_ENDS = [
    'auto',
    'kilo',
    'memo',
    'photo',
    'piano',
    'pimento',
    'pro',
    'solo',
    'soprano'
]


def pluralize(word: str = None, count: int = 1):
    if not word:
        return ''
    if count <= 1 or len(word) < 3:
        return word

    plural = ABERRANT_PLURAL_MAP.get(word, None)
    if plural:
        return plural

    try:
        if word[-1] == 'y' and word[-2] not in VOWELS:
            return word[:-1] + 'ies'
        if word[-2:] == 'is':
            return word[:-2] + 'es'
        if word[-2:] == 'us':
            return word[:-2] + 'i'
        if word[-2:] == 'on' or word[-2:] == 'um':
            return word[:-2] + 'a'
        if word[-1] == 'x':
            return word + 'es'
        if word[-1] == 'o':
            if word in NORMAL_O_ENDS or word[-2] in VOWELS:
                return word + 's'
            return word + 'es'
        if word[-1] == 'f':
            return word[:-1] + 'ves'
        if word[-2:] == 'fe':
            return word[:-2] + 'ves'
        if word[-1] == 's':
            if word[-2] in VOWELS:
                if word[-3:] == 'ius':
                    return word[:-2] + 'ises'
                return word[:-1] + 'ses'
            return word + 'es'
        if word[-2:] in ('ch', 'sh'):
            return word + 'es'
    except Exception as err:
        log('pluralize', err)
        pass
    return word + 's'
