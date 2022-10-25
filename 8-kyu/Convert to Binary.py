"""
@File    : Convert to Binary.py 
@Author  : Richie Black
@Time    : 25.10.2022 18:48

I have been learning Python since August 2022.
"""


def to_binary(n):
    return int(bin(n)[2::])


"""Best practices
-----------------

def to_binary(n):
    return int(f'{n:b}')

-----------------

def to_binary(n):
    return int(bin(n)[2:])

-----------------

def to_binary(n):
    return int(format(n, 'b'))

-----------------
"""

# https://www.codewars.com/kata/reviews/5fe57760ad87de0001fbeb02/groups/632c5cf27db83600014e8f8c
