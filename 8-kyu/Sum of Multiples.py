"""
@File    : Sum of Multiples.py 
@Author  : Richie Black
@Time    : 28.10.2022 19:59

I have been learning Python since August 2022.
"""


def sum_mul(n, m):
    sum = 0

    if n < 1 or m < 1:
        return 'INVALID'

    for i in range(n, m):
        if not i % n:
            sum += i
    return sum


"""Best practices
-----------------

def sum_mul(n, m):
    if m > 0 and n > 0:
        return sum(range(n, m, n))
    else:
        return 'INVALID'

-----------------

def sum_mul(n, m):
    return sum(x for x in range(n, m, n)) if m > 0 and n > 0 else 'INVALID'

-----------------

def sum_mul(n, m):
    return sum(range(n, m, n)) if n > 0 and m > 0 else "INVALID"

-------------
"""

# https://www.codewars.com/kata/reviews/5772a363a95d044c7c0001bb/groups/6335e5c9ee5fc70001ae13f1
