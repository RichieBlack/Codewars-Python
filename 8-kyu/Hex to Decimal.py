"""
@File    : Hex to Decimal.py 
@Author  : Richie Black
@Time    : 25.10.2022 18:58

I have been learning Python since August 2022.
"""


def hex_to_dec(s):
    return int(s, base=16)


"""Best practices
-----------------

def hex_to_dec(s):
    return int(s, 16)

-----------------

from functools import partial


hex_to_dec = partial(int, base=16)

-----------------

def hex_to_dec(s):
    key = "0123456789abcdef"
    n=0
    res=0
    for l in s[::-1]:
        res += key.index(l)*(16.**n)
        n+=1
        
    return int(res)

-----------------

hex_to_dec = lambda s:int(s, 16)

-----------------
"""

# https://www.codewars.com/kata/reviews/57a5aa21e08254d7a400010f/groups/632c7cb096b89c00014870b5
