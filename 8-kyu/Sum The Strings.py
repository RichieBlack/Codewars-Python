"""
@File    : Sum The Strings.py 
@Author  : Richie Black
@Time    : 21.10.2022 21:30

I have been learning Python since August 2022.
"""


def sum_str(a, b):
    if a == "": a = a.replace("", "0")
    if b == "": b = b.replace("", "0")
    return str(int(int(a) + int(b)))


"""Best practices
-----------------

def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))

-----------------

def sum_str(a, b):
    return str(int('0' + a) + int('0' + b))

-----------------

def sum_str(*values):
    return str(sum(int(s or '0') for s in values))

-----------------
"""

# https://www.codewars.com/kata/reviews/5970d50a3afee564d30000cd/groups/63297d4e7107960001c7523c
