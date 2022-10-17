# https://www.codewars.com/kata/reviews/57059fdddbf09446a800006b/groups/57628ed53aabbbee14000ecf

def is_uppercase(inp):
    caps = inp.upper()
    if caps == inp:
        return True
    else:
        return False


# I have been studying Python for one month.

"""Best practices
-----------------

def is_uppercase(inp):
    return inp.upper() == inp

-----------------
from re import search


def is_uppercase(inp):
    if search(r'[a-z]', inp):
        return False
    return True

-----------------
"""
