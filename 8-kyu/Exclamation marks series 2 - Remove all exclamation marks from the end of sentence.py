"""
@File    : Exclamation marks series 2 - Remove all exclamation marks from the end of sentence.py 
@Author  : Richie Black
@Time    : 28.10.2022 19:49

I have been learning Python since August 2022.
"""


def remove(s):
    for i in range(len(s)):
        if s.endswith('!'):
            s = s[:-1]
        else:
            return s


"""Best practices
-----------------

def remove(s):
    return s.rstrip("!")

-----------------

def remove(s):
    while s and s[-1] == "!":
        s = s[:-1]
    return s

-----------------

import re


def remove(s):
    return re.match(r"(.*[^!]+)\!*", s).group(1)

-------------
"""

# https://www.codewars.com/kata/reviews/5804fa524c94b82b760000a4/groups/6335a4cfe71ee20001b94fa5
