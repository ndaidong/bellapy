#!/usr/bin/env python3

import string
import hashlib

from random import shuffle, choice


def genid(count=16, prefix=''):
    alphadigits = string.ascii_letters + string.digits
    alphadigits_list = list(alphadigits)
    shuffle(alphadigits_list)
    alphadigits = ''.join(alphadigits_list)
    leng = count - len(prefix)
    if leng < 0:
        return prefix
    return prefix + ''.join([choice(alphadigits) for n in range(leng)])


def _xhash(txt='', algorithm='md5'):
    if not txt:
        return ''
    if algorithm == 'ripemd160':
        m = hashlib.new('ripemd160')
    else:
        m = hashlib.md5()
    m.update(str(txt).encode('utf-8'))
    return m.hexdigest()


def md5(txt=''):
    return _xhash(txt, md5)


def md160(txt=''):
    return _xhash(txt, 'ripemd160')


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


def pluralize(word=None, count=1):
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
        print(err)
        pass
    return word + 's'
