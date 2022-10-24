"""
@File    : To square(root) or not to square(root).py 
@Author  : Richie Black
@Time    : 24.10.2022 22:40

I have been learning Python since August 2022.
"""


def square_or_square_root(arr):
    root = []
    for i in arr:
        if i ** 0.5 == int(i ** 0.5):
            root.append(int(i ** 0.5))
        else:
            root.append(int(i ** 2))
    return root


"""Best practices
-----------------

def square_or_square_root(arr):
    result = []
    for x in arr:
        root = x ** 0.5
        if root.is_integer():
            result.append(root)
        else:
            result.append(x * x)
    return result

-----------------

from math import sqrt


def square_or_square_root(arr):
    return [int(sqrt(a)) if sqrt(a) % 1 == 0 else a ** 2 for a in arr]

-----------------

def square_or_square_root(arr):
    return [i ** 0.5 if (i ** 0.5).is_integer() else i ** 2 for i in arr]

-----------------

def square_or_square_root(arr):
    return [n * n if n ** 0.5 % 1 else n ** 0.5 for n in arr]
    
-----------------

square_or_square_root = lambda a: [not n ** .5 % 1 and int(n ** .5)or n ** 2 for n in a]

-----------------
"""

# https://www.codewars.com/kata/reviews/57fc101a777d18cc37000113/groups/632b1dfec950940001d7f266
