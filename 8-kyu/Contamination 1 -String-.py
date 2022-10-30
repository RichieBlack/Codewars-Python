"""
@File    : Contamination 1 -String-.py 
@Author  : Richie Black
@Time    : 30.10.2022 23:41

I have been learning Python since August 2022.
"""


def contamination(text, char):
    if text:
        return char * len(text)
    else:
        return text


"""Best practices
-----------------

def contamination(text, char):
  return char * len(text)

-----------------

import re


def contamination(text, char):
  return re.sub(".", char, text)

-----------------

contamination = lambda s, c: c * len(s)

-----------------
"""

# https://www.codewars.com/kata/reviews/596fba6c74dd684086000004/groups/634ec15b46ebd50001ae22d6
