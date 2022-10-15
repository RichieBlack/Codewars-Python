# link: https://www.codewars.com/kata/reviews/5f9f43cf76df000001b373c1/groups/61b67986c2c0be0001ad3ba7

def approx_equals(a, b):
    a = round(a, 6)
    b = round(b, 6)
    return abs(a - b) < 0.001

# I have been studying Python for one month.

'''
Best practices
--------------

def approx_equals(a, b):
    return abs(a-b) < 0.001

--------------

from math import isclose

def approx_equals(a, b):
    return isclose(a, b, rel_tol=0, abs_tol=1e-3)

--------------

approx_equals = lambda a, b: abs(a - b) < .001

--------------
'''
