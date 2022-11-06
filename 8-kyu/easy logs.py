"""
@File    : easy logs.py 
@Author  : Richie Black
@Time    : 06.11.2022 20:07

I have been learning Python since August 2022.
"""

import math


def logs(x, a, b):
    return math.log(a, x) + math.log(b, x)


"""Best practices
-----------------

from math import log


def logs(x, a, b):
    return log(a * b, x)

-----------------

from math import log

def logs(x, a, b):
    return log(a, x) + log(b, x)

-----------------

logs = lambda x, a, b, l = __import__("math").log: l(a, x) + l(b,x)

-----------------
"""

# https://www.codewars.com/kata/reviews/5b69c2b6f906a9089c000cff/groups/6367dc9224301d00018ac27d