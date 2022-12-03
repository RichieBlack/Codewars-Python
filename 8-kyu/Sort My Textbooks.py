"""
@File    : Sort My Textbooks.py 
@Author  : Richie Black
@Time    : 03.12.2022 19:38

I have been learning Python since August 2022.
"""


def sorter(textbooks):
    textbooks.sort(key=str.lower)

    return textbooks


"""Best practices
-----------------

def sorter(textbooks):
    return sorted(textbooks,key=str.lower)

-----------------

def sorter(textbooks):
    return sorted(textbooks, key=str.casefold)

-----------------

def sorter(textbooks):
    return sorted(textbooks, key=lambda arg: arg.lower())

-----------------
"""

# https://www.codewars.com/kata/reviews/5a07e5c35dcd43adea0007a4/groups/638b6d4c2e6f410001edfce0
