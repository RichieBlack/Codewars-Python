"""
@File    : Capitalization and Mutability.py 
@Author  : Richie Black
@Time    : 22.10.2022 20:32

I have been learning Python since August 2022.
"""


def capitalize_word(word):
    return "".join(word[0].upper() + word[1::])


"""Best practices
-----------------

def capitalizeWord(word):
    return word.capitalize()

-----------------

def capitalizeWord(s):
    return s.title()

-----------------

def capitalizeWord(word):
    return word[0].upper() + word[1:]

-----------------
"""

# https://www.codewars.com/kata/reviews/5c2400cf18e7b6279900042b/groups/6329bed47107960001c766a6
