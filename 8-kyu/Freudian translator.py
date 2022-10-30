"""
@File    : Freudian translator.py 
@Author  : Richie Black
@Time    : 30.10.2022 23:22

I have been learning Python since August 2022.
"""


def to_freud(sentence):
    """The function will take a string as its argument,
    and return a string with every word replaced by the explanation to everything,
    according to Freud.

    Note that an empty string, or no arguments, should return an empty string.
    """
    freud = []
    if sentence:
        for word in sentence.split():
            word = "sex"
            freud.append(word)
        return ' '.join(freud)
    else:
        return sentence


"""Best practices
-----------------

def to_freud(sentence):
    return ' '.join('sex' for _ in sentence.split())

-----------------

def to_freud(s):
    return (len(s.split()) * "sex ").strip()

-----------------

import re


def to_freud(sentence):
    return re.sub('\S+', 'sex', sentence)

-----------------
"""

# https://www.codewars.com/kata/reviews/5720b0270a7cb839d200001d/groups/634d7ac7ffbdb50001ff7c1e
