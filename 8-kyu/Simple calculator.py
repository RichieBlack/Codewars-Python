"""
@File    : Simple calculator.py 
@Author  : Richie Black
@Time    : 29.10.2022 11:11

I have been learning Python since August 2022.
"""


def calculator(x, y, op):
    if isinstance(x, int) and isinstance(y, int):
        if op == '+':
            return x + y
        elif op == '-':
            return x - y
        elif op == '*':
            return x * y
        elif op == '/':
            return x / y
        else:
            return "unknown value"
    else:
        return "unknown value"


"""Best practices
-----------------

def calculator(x, y, op):
  return eval(f'{x}{op}{y}') if type(x) == type(y) == int and str(op) in '+-*/' else 'unknown value'

-----------------

def calculator(x, y, op):
    try:
        assert op in "+-*/"
        return eval('%d%s%d' % (x, op, y))
    except:
        return "unknown value"

-----------------

def calculator(x, y, op):
    try:
        return {'+': x + y, '-': x - y, '*': x * y, '/': x / y}[op]
    except (TypeError, KeyError): 
        return 'unknown value'

-----------------

import operator
from functools import reduce

OPS = {
    "+": operator.__add__,
    "-": operator.__sub__,
    "*": operator.__mul__,
    "/": operator.__truediv__
}


def calculator(x, y, op):
    return reduce(OPS[op], (x, y)) if op in OPS and type(x) is type(y) is int else 'unknown value'
    
-----------------  
"""

# https://www.codewars.com/kata/reviews/59bc5c31590b86955e00057b/groups/633f473fff928300014839cc
