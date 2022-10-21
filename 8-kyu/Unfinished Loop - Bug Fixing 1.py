"""
@File    : Unfinished Loop - Bug Fixing 1.py 
@Author  : Richie Black
@Time    : 21.10.2022 21:33

I have been learning Python since August 2022.
"""


def create_array(n):
    res = []

    for i in range(1, n + 1): res += [i]

    return res


"""Best practices
-----------------

def create_array(n):
    res = []
    i = 1
    while i <= n:
        res += [i]
        i += 1
    return res

-----------------

def create_array(n):
    return [i for i in range(1, n + 1)]

-----------------

create_array = lambda n: list(range(1, n + 1))

-----------------
"""

# https://www.codewars.com/kata/reviews/55c8779d285492f06d000032/groups/63298401f5f54000010c4285
