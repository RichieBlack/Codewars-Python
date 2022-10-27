"""
@File    : SpeedCode 2 - Array Madness.py 
@Author  : Richie Black
@Time    : 27.10.2022 14:01

I have been learning Python since August 2022.
"""


def array_madness(a, b):
    sum_a = 0
    sum_b = 0

    for i in a:
        sum_a = sum_a + i ** 2
    for i in b:
        sum_b = sum_b + i ** 3

    return sum_a > sum_b


"""Best practices
-----------------

def array_madness(a,b):
    return sum(x ** 2 for x in a) > sum(x ** 3 for x in b)

-----------------

def array_madness(a,b):
    return sum(map(lambda a: a ** 2, a)) > sum(map(lambda b: b ** 3, b))

-----------------

def array_madness(a,b):
    sa = 0
    sb = 0
    for i in range(0,len(a)):
        sa += a[i] ** 2
    for i in range(0,len(b)):
        sb += b[i] ** 3
    return sa > sb

-----------------
"""

# https://www.codewars.com/kata/reviews/59b1f74e27f707b5830000f0/groups/6332148f09fe2100015d1154
