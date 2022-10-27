"""
@File    : No zeros for heros.py 
@Author  : Richie Black
@Time    : 27.10.2022 14:09

I have been learning Python since August 2022.
"""


def no_boring_zeros(n):
    res = n

    for i in range(len(str(n))):
        if not res % 10:
            res = res / 10
        else:
            return res

    return 0


"""Best practices
-----------------

def no_boring_zeros(n):
    try:
        return int(str(n).rstrip('0'))
    except ValueError:
        return 0

-----------------

def no_boring_zeros(n):
    if n == 0:
        return n
    while n % 10 == 0:
        n = n / 10
    return n

-----------------

def no_boring_zeros(n):
    return int(str(n).strip("0")) if n else n

-----------------

def no_boring_zeros(n):
    return int(str(n).strip('0') or 0)
    
-----------------
"""

# https://www.codewars.com/kata/reviews/570b7c040002c29e1e00006f/groups/6332ee17b3b9030001a4640a
