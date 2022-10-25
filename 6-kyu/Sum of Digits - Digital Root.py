"""
@File    : Sum of Digits - Digital Root.py 
@Author  : Richie Black
@Time    : 25.10.2022 20:02

I have been learning Python since August 2022.
"""


def digital_root(n):
    return n if n < 10 else digital_root(sum([int(i) for i in str(n)]))


"""Best practices
-----------------

def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int, str(n))))

-----------------

def digital_root(n):
    return n % 9 or n and 9 

-----------------

def digital_root(n):
    while n > 9:
        n = sum(map(int, str(n)))
    return n

-----------------
"""

# https://www.codewars.com/kata/reviews/541c8b5e7e4b4c61e2000153/groups/63581056b8a6900001de39f1
