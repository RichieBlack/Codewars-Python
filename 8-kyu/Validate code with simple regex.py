"""
@File    : Validate code with simple regex.py 
@Author  : Richie Black
@Time    : 29.10.2022 11:51

I have been learning Python since August 2022.
"""

import re


def validate_code(code):
    return True if (re.search('^[1-3]', str(code))) else False


"""Best practices
-----------------

def validate_code(code):
    return str(code).startswith(('1', '2', '3'))

-----------------

def validate_code(code):
    return str(code)[0] in '123'

-----------------

import re

def validate_code(code):
    return bool(re.match(r"^[123]\d*$", str(code)))

-----------------

import re


def validate_code(code):    
    return bool(re.match('[123]', str(code)))

"""

# https://www.codewars.com/kata/reviews/56a29076db22b376ea000007/groups/6342dd2442231700011ea6b1
