"""
@File    : Vowel remover.py 
@Author  : Richie Black
@Time    : 25.10.2022 12:57

I have been learning Python since August 2022.
"""


def shortcut(s):
    return ''.join([i for i in s if not i in 'aeiou'])


"""Best practices
-----------------

def shortcut(s):
    return s.translate(None, 'aeiou')

-----------------

def shortcut(s):
    return ''.join(c for c in s if c not in 'aeiou')

-----------------

def shortcut( s ):
    for vowel in "aeiou":
        s = s.replace(vowel, "")
    return s

-----------------

import re


def shortcut( s ):
    return re.sub('[aoeui]', '', s)

-----------------

import re


shortcut = lambda s: re.sub('[aeiou]', '', s)

-----------------
"""

# https://www.codewars.com/kata/reviews/5577325c7bfb9226da000043/groups/632c37997db83600014e85c8
