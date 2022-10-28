"""
@File    : Regex count lowercase letters.py 
@Author  : Richie Black
@Time    : 29.10.2022 0:58

I have been learning Python since August 2022.
"""

import re


def lowercase_count(strng):
    return len(re.findall('[a-z]', strng))


"""Best practices
-----------------

def lowercase_count(strng):
    return sum(a.islower() for a in strng)

-----------------

import re


def lowercase_count(string):
    return len(re.findall('[a-z]',string))

-----------------

def lowercase_count(str):
    return sum(1 for c in str if c.islower())

-----------------
"""

# https://www.codewars.com/kata/reviews/56aa5c08828bed821f00002f/groups/633df32d7471ff000191e1f5
