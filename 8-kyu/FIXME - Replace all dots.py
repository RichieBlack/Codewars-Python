"""
@File    : FIX ME - Replace all dots.py
@Author  : Richie Black
@Time    : 24.10.2022 22:44

I have been learning Python since August 2022.
"""

import re


def replace_dots(str):
    return re.sub(r'[.]', '-', str)


"""Best practices
-----------------

def replace_dots(string):
    return string.replace('.', '-')

-----------------

import re


def replace_dots(str):
    return re.sub(r"\.", "-", str)

-----------------

replace_dots = lambda x: x.replace(".", "-")

-----------------
"""

# https://www.codewars.com/kata/reviews/5972cebcabb32828300000c2/groups/632b25fac950940001d7f53e
