"""
@File    : Parse nice int from char problem.py 
@Author  : Richie Black
@Time    : 20.10.2022 21:35

I have been learning Python since August 2022.
"""


def get_age(age):
    return int(age[0])


"""Best practices
-----------------

def get_age(age):
    return int(age[0])

-----------------

import re


def get_age(age):
    return int(re.search(r"\d+", age).group())

-----------------

def get_age(age):
    for x in age:
        if x.isdigit():
            return int(x) 

-----------------
"""

# https://www.codewars.com/kata/reviews/57dee998dd9e2b5072000039/groups/63284822c032e000019b9d81
