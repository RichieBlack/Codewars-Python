"""
@File    : Did she say hallo.py 
@Author  : Richie Black
@Time    : 29.10.2022 11:54

I have been learning Python since August 2022.
"""


def validate_hello(greetings):
    hello = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'czesc', 'ahoj']

    for i in hello:
        if i in greetings.lower():
            return True
    else:
        return False


"""Best practices
-----------------

def validate_hello(greetings):
    return any(x in greetings.lower() for x in ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc'])

-----------------

from re import compile, search, I

REGEX = compile(r'hello|ciao|salut|hallo|hola|ahoj|czesc', I)


def validate_hello(greeting):
    return bool(search(REGEX, greeting))

-----------------

import re


def validate_hello(greetings):
    return bool(re.search("h[ae]llo|ciao|salut|hola|ahoj|czesc", greetings.lower()))

-----------------

def validate_hello(greetings):
    g = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    for s in g:
        if s in greetings.lower():
            return True
    return False
    
-----------------
"""

# https://www.codewars.com/kata/reviews/56a641ef333e5367f300001e/groups/6342f15f42231700011eab62
