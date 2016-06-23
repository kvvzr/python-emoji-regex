# -*- coding: utf-8 -*-

import re
import sys

def compile():
    if sys.version_info >= (3, 0):
        with open('emojis.txt') as f:
            raw_regex = ''.join(f.readlines()).strip()
    else:
        with open('emojis.v2.txt') as f:
            raw_regex = ''.join(f.readlines()).strip()
        raw_regex = raw_regex.decode('raw_unicode_escape')

    return re.compile(raw_regex)

compile()
