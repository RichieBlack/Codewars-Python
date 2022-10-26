"""
@File    : Exclamation marks series 11 - Replace all vowel to exclamation mark in the sentence.py 
@Author  : Richie Black
@Time    : 26.10.2022 20:48

I have been learning Python since August 2022.
"""


def replace_exclamation(s):
    return "".join(["!" if char in "aeiouAEIOU" else char for char in s])


"""Best practices
-----------------

def replace_exclamation(s):
    return ''.join('!' if c in 'aeiouAEIOU' else c for c in s)

-----------------

import re


def replace_exclamation(s):
    return re.sub('[aeiouAEIOU]', '!', s)

-----------------

def replace_exclamation(s):
    return s.translate(str.maketrans('aeiouAEIOU', '!' * 10))

-----------------
"""

# https://www.codewars.com/kata/reviews/5851ee407d608bbb01000df6/groups/632df4488f14580001903754
