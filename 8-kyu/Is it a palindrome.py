"""
@File    : Is it a palindrome.py 
@Author  : Richie Black
@Time    : 22.10.2022 20:34

I have been learning Python since August 2022.
"""


def is_palindrome(s):
    return s.lower() == s[::-1].lower()


"""Best practices
-----------------

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

-----------------

def is_palindrome(s):
    return s.lower() == s[::-1].lower()

-----------------

is_palindrome=lambda x: x.lower() ==x [::-1].lower()

-----------------
"""

# https://www.codewars.com/kata/reviews/5d56ce41d0461900017b19d1/groups/6329c1037107960001c76706
