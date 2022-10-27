"""
@File    : String Templates - Bug Fixing 5.py 
@Author  : Richie Black
@Time    : 27.10.2022 14:23

I have been learning Python since August 2022.
"""


def build_string(*args):
    return "I like {}!".format(", ".join(args))


"""Best practices
-----------------

def build_string(*args):
    return "I like {}!".format(", ".join(args))

-----------------

def build_string(*args):
    return f"I like {', '.join(args)}!"

-----------------

build_string = lambda *args: "I like {}!".format(", ".join(args))

-----------------
"""

# https://www.codewars.com/kata/reviews/55c97c5cc941432d52000098/groups/633424f36c9f86000178fe03
