# link: https://www.codewars.com/kata/reviews/5806763a0be9a293e40000da/groups/61f8f70f3e263f0001790511

def grow(arr):
    multi = 1
    for i in arr:
        multi *= i
    return multi


'''
Best practices
--------------

def grow(arr):
    product = 1
    for i in arr:
        product *= i
    return product

--------------

from functools import reduce

def grow(arr):
    return reduce(lambda x, y: x * y, arr)

--------------

import math

def grow(arr):
    return math.prod(arr)

--------------

def grow(arr):
    return eval('*'.join([str(i) for i in arr]))

--------------
'''
