"""
@File    : What's the real floor.py 
@Author  : Richie Black
@Time    : 22.10.2022 20:52

I have been learning Python since August 2022.
"""


def get_real_floor(n):
    if n > 13:
        return n - 2
    elif n >= 1:
        return n - 1
    else:
        return n


"""Best practices
-----------------

def get_real_floor(n):
    if n <= 0: return n
    if n < 13: return n-1
    if n > 13: return n-2

-----------------

def get_real_floor(n):
    return n if n < 1 else n - 1 if n < 13 else n - 2

-----------------

def get_real_floor(n):
    return n - (n > 0) - (n > 13)

-----------------
"""

# https://www.codewars.com/kata/reviews/57a14f60cd55e97bcd000027/groups/632a2baa7107960001c78391
