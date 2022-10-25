"""
@File    : Is this my tail.py 
@Author  : Richie Black
@Time    : 25.10.2022 18:56

I have been learning Python since August 2022.
"""


def correct_tail(body, tail):
    return True if body[-1] == tail else False


"""Best practices
-----------------

def correct_tail(body, tail):
    return body.endswith(tail)

-----------------

def correct_tail(body, tail):
    return body[-1] == tail

-----------------

correct_tail = str.endswith

-----------------
"""

# https://www.codewars.com/kata/reviews/56f7d47f1dc33806c8000071/groups/632c77687db83600014e96d2
