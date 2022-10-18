# https://www.codewars.com/kata/reviews/58058ba934d14b2f15000006/groups/58059acdf5c9501e120000b7

def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"


# I have been studying Python for one month.

"""Best practices
-----------------

def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"

-----------------

def greet(name, owner):
    return "Hello {}".format("boss" if name == owner else "guest")

-----------------

def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"

-----------------
"""
