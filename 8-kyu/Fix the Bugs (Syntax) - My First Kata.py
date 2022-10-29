"""
@File    : Fix the Bugs (Syntax) - My First Kata.py 
@Author  : Richie Black
@Time    : 29.10.2022 11:45

I have been learning Python since August 2022.
"""


def my_first_kata(a, b):
    if not (isinstance(a, int) and isinstance(b, int)) or (isinstance(a, bool) or isinstance(b, bool)):
        return False
    else:
        return a % b + b % a


"""Best practices
-----------------

def my_first_kata(a,b):
    if type(a) == int and type(b) == int:
        return a % b + b % a
    else:
        return False

-----------------

def my_first_kata(a, b):
    try:
        return a % b + b % a
    except (TypeError, ZeroDivisionError):
        return False

-----------------

def my_first_kata(a,b):
    if type(a) == int and type(b) == int: return a % b + b % a
    return False

-----------------

def my_first_kata(a,b):
    return a % b + b % a if type(a) is int and type(b) is int else False
    
-----------------
"""

# https://www.codewars.com/kata/reviews/56c9906d186f8221a0000037/groups/63421097df19f700014724e2
