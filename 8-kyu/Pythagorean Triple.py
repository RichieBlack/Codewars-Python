"""
@File    : Pythagorean Triple.py 
@Author  : Richie Black
@Time    : 28.11.2022 1:45

I have been learning Python since August 2022.
"""


def pythagorean_triple(integers):
    if integers[0] ** 2 == integers[1] ** 2 + integers[2] ** 2:
        return True

    elif integers[1] ** 2 == integers[2] ** 2 + integers[0] ** 2:
        return True

    elif integers[2] ** 2 == integers[0] ** 2 + integers[1] ** 2:
        return True

    else:
        return False


"""Best practices
-----------------

def pythagorean_triple(integers):
    a, b, c = sorted(integers)
    return a * a + b * b == c * c

-----------------

def pythagorean_triple(arr): 
    arr = sorted(arr); # sorted array
    return arr[0] ** 2 + arr[1] ** 2 == arr[2] ** 2

-----------------

def pythagorean_triple(i):
    m = i.pop(i.index(max(i)))
    return i[0] ** 2 + i[1] ** 2 == m ** 2

-----------------
"""

# https://www.codewars.com/kata/reviews/5951e5b027f98047c60000ac/groups/6383db5a30362100012c281c