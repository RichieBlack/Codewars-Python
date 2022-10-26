"""
@File    : String cleaning.py 
@Author  : Richie Black
@Time    : 26.10.2022 21:38

I have been learning Python since August 2022.
"""


def string_clean(s):
    return "".join(["" if num in "0123456789" else num for num in s])


"""Best practices
-----------------

def string_clean(s):
    return ''.join(x for x in s if not x.isdigit())

-----------------

import re


def string_clean(s):
    return re.sub(r'\d', '', s)

-----------------

def string_clean(s):
    for d in '0123456789':
        s = s.replace(d, '')
    return s

-----------------
"""

# https://www.codewars.com/kata/reviews/57e1e62bd8d1c76a24000083/groups/632df769ee1c3f00017f54a7
