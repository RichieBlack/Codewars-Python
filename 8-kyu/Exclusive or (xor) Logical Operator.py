"""
@File    : Exclusive or (xor) Logical Operator.py 
@Author  : Richie Black
@Time    : 25.10.2022 18:46

I have been learning Python since August 2022.
"""


def xor(a, b):
    if a == b:
        return False
    else:
        return True


"""Best practices
-----------------

def xor(a,b):
    return a != b

-----------------

def xor(a,b):
    return a ^ b

-----------------

from operator import xor

-----------------

def xor(a,b):
    return a is not b
    
-----------------
"""

# https://www.codewars.com/kata/reviews/56fb48d137fb7ca8d6000009/groups/632c5a597159d6000186617e
