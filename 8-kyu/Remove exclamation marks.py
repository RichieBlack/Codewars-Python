"""
@File    : Remove exclamation marks.py 
@Author  : Richie Black
@Time    : 20.10.2022 3:49

I have been learning Python since August 2022.
"""


def remove_exclamation_marks(s):
    return s.replace("!", "") if "!" in s else s


"""Best practices
-----------------

def remove_exclamation_marks(s):
    return s.replace('!', '')

-----------------

def remove_exclamation_marks(s):
    return ''.join([x for x in s if x != '!'])

-----------------

def remove_exclamation_marks(s):
    new_s = ''
    for i in s:
        if i != '!':
            new_s += i
    return new_s

-----------------
"""

# https://www.codewars.com/kata/reviews/57fa28a64f0caf8b4b000044/groups/62123b5f8c41bd0001381091
