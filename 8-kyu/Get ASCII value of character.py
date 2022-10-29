"""
@File    : Get ASCII value of character.py 
@Author  : Richie Black
@Time    : 29.10.2022 12:00

I have been learning Python since August 2022.
"""


def get_ascii(c):
    return ord(c)


"""Best practices
-----------------

def get_ascii(c):
   return ord(c)

-----------------

get_ascii = ord

-----------------

def get_ascii(c):
    return bytearray(c.encode('ascii'))[0]

-----------------
"""

# https://www.codewars.com/kata/reviews/5e71ebea76b67f0001b01ec1/groups/63432b59bc48e500013de0d5
