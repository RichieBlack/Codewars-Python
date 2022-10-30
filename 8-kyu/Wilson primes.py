"""
@File    : Wilson primes.py 
@Author  : Richie Black
@Time    : 30.10.2022 14:20

I have been learning Python since August 2022.
"""


def am_i_wilson(n):
    return n in (5, 13, 563)


"""Best practices
-----------------

def am_i_wilson(n):
   #Piece of shit instead of code for piece of shit instead of instructions. 
   #It is really hard to imagine even worse exercise than this for 8 kyu.
   #Extreamly outdated for 2019 it no longer has place in here. 
    return True if n == 5 or n == 13 or n == 563 else False

-----------------

# this is not 8 kyu, not programming, not even math.
# this is 'google it, then hardcode it'.
# leave this to neural nets, don't solve it in a browser.
def am_i_wilson(n):
    return n in [5, 13, 563]

-----------------
"""

# https://www.codewars.com/kata/reviews/5618c077d74136ae3c0000bd/groups/63433fe7fe5d8100015e5d02
