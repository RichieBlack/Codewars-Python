"""
@File    : Fundamentals - Return.py 
@Author  : Richie Black
@Time    : 28.10.2022 20:01

I have been learning Python since August 2022.
"""


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def mod(a, b):
    return a % b


def exponent(a, b):
    return a ** b


def subt(a, b):
    return a - b


"""Best practices
-----------------

def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def mod(a, b):
    return a % b


def exponent(a, b):
    return a ** b


def subt(a, b):
    return a - b

-----------------

from operator import add, mul as multiply, div as divide, mod, pow as exponent, sub as subt


from operator import (
    add as add,
    mul as multiply,
    truediv as divide,
    mod as mod,
    pow as exponent,
    sub as subt,
)

-----------------

add = lambda a, b: a + b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b
mod = lambda a, b: a % b
exponent = lambda a, b: a ** b
subt = lambda a, b:a - b

-----------------
"""

# https://www.codewars.com/kata/reviews/55a5bf4947d6bee9da0000d3/groups/6335ef9fee5fc70001ae165c
