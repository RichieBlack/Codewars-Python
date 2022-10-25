"""
@File    : Find Multiples of a Number.py 
@Author  : Richie Black
@Time    : 25.10.2022 12:55

I have been learning Python since August 2022.
"""


def find_multiples(integer, limit):
    return ([i for i in range(integer, limit + 1) if not i % integer])


"""Best practices
-----------------

def find_multiples(integer, limit):
    return list(range(integer, limit+1, integer))

-----------------

def find_multiples(integer, limit):
    arr = []
    count = integer
    while count <= limit:
        arr.append(count)
        count += integer
    return arr

-----------------

def find_multiples(integer, limit):
    return [i for i in range(integer, limit + 1, integer)]

-----------------

find_multiples = lambda a, b: list(range(a, b + 1, a))

-----------------
"""

# https://www.codewars.com/kata/reviews/58ca6596c0d6401f27000463/groups/632c20d17db83600014e7f40
