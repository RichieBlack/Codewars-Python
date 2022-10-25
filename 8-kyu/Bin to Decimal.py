"""
@File    : Bin to Decimal.py 
@Author  : Richie Black
@Time    : 25.10.2022 19:14

I have been learning Python since August 2022.
"""


def bin_to_decimal(inp):
    return int(inp, base=2)


"""Best practices
-----------------

def bin_to_decimal(inp):
    return int(inp, 2)

-----------------

def bin_to_decimal(inp):
    num = 0
    inp = inp[::-1]
    for i in range(len(inp)):
        num += int(inp[i]) * 2 ** i
    return num

-----------------

bin_to_decimal = lambda inp: int(inp, 2)

-----------------
"""

# https://www.codewars.com/kata/reviews/57a5dcdaea0b79f775000167/groups/632c8b37dcc8310001272f47
