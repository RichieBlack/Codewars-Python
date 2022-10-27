"""
@File    : Pre-FizzBuzz Workout 1.py 
@Author  : Richie Black
@Time    : 27.10.2022 7:23

I have been learning Python since August 2022.
"""


def pre_fizz(n):
    return [x for x in range(1, n + 1)]


"""Best practices
-----------------

def pre_fizz(n):
    return list(range(1, n + 1))

-----------------

def pre_fizz(n):
    return [x for x in range(1, n + 1)]

-----------------

pre_fizz = lambda n: list(range(1, n + 1))

-----------------
"""

# https://www.codewars.com/kata/reviews/57bb82357188e1e211000111/groups/633067ad1f92810001aa0851
