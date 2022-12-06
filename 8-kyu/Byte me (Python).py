"""
@File    : Byte me (Python).py 
@Author  : Richie Black
@Time    : 06.12.2022 19:35

I have been learning Python since August 2022.
"""

import sys


def total_bytes(object):
    return sys.getsizeof(object)


"""Best practices
-----------------

import sys


def total_bytes(object):
    return sys.getsizeof(object)

-----------------

from sys import getsizeof as total_bytes

-----------------

total_bytes = __import__('sys').getsizeof

-----------------
"""

# https://www.codewars.com/kata/reviews/636f2a10956dde0001a5aef1/groups/638f4eee0036f0000198094a
