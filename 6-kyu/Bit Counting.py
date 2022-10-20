"""
@File    : Bit Counting.py 
@Author  : Richie Black
@Time    : 20.10.2022 3:45

I have been learning Python since August 2022.
"""


def count_bits(n):
    count = 0
    while (n > 0):
        if n % 2:
            count += 1
        n //= 2
    return count


"""Best practices
-----------------

def countBits(n):
    return bin(n).count("1")

-----------------

def countBits(n):
    total = 0
    while n > 0:
        total += n % 2
        n >>= 1
    return total

-----------------

def countBits(n):
    return '{:b}'.format(n).count('1')

-----------------
"""

# https://www.codewars.com/kata/reviews/54909b9defb59728f600016f/groups/6325ce37faa0b60001e2c52c
