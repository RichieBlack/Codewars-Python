"""
@File    : Is it a number.py 
@Author  : Richie Black
@Time    : 28.10.2022 20:04

I have been learning Python since August 2022.
"""


def isDigit(string):
    try:
        float(string)
        return True
    except:
        return False


"""Best practices
-----------------

def isDigit(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

-----------------

def isDigit(string):
    return string.lstrip('-').replace('.','').isdigit()

-----------------

from re import match


def isDigit(string):
    return bool(match(r"^[-+]?\d+\.?\d*?$", string))

-----------------
"""

# https://www.codewars.com/kata/reviews/5775805f60a1c30a19000030/groups/6335f585ff648200019693f9
