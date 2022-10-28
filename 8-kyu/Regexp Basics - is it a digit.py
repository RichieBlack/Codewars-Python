"""
@File    : Regexp Basics - is it a digit.py 
@Author  : Richie Black
@Time    : 28.10.2022 19:46

I have been learning Python since August 2022.
"""

import re


def is_digit(n):
    match = re.findall('[\d]', n)
    return match[0] == n if match else False


"""Best practices
-----------------

def is_digit(n):
    return n.isdigit() and len(n) == 1

-----------------

import re


def is_digit(n):
    return bool(re.match("\d\Z", n))

-----------------

is_digit=lambda n: len(n)==1 and n in "0123456789"

-------------

is_digit = set("1234567890").__contains__

-------------
"""

# https://www.codewars.com/kata/reviews/569c0ab2269589c328000047/groups/63358d4f3e91f7000188d0d7
