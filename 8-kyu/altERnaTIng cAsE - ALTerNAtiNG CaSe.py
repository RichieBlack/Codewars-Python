"""
@File    : altERnaTIng cAsE - ALTerNAtiNG CaSe.py 
@Author  : Richie Black
@Time    : 20.10.2022 21:43

I have been learning Python since August 2022.
"""


def to_alternating_case(string):
    return "".join([letter.swapcase() for letter in string])


"""Best practices
-----------------

def to_alternating_case(string):
    return string.swapcase()

-----------------

def to_alternating_case(string):
    return ''.join([c.upper() if c.islower() else c.lower() for c in string])

-----------------

to_alternating_case = str.swapcase

-----------------
"""

# https://www.codewars.com/kata/reviews/56f0036e39054c54a6000014/groups/632882f376176900017428e5
