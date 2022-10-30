"""
@File    : Jaden Casing Strings.py
@Author  : Richie Black
@Time    : 26.10.2022 20:17

I have been learning Python since August 2022.
"""


def to_jaden_case(string):
    x = string.split()
    n = []

    for i in x:
        n.append(str(i).capitalize())
    return ' '.join(n)


'''
Best practices
--------------
import string
toJadenCase = string.capwords

--------------
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())
'''

# https://www.codewars.com/kata/reviews/54176ef96a4e100f28000068/groups/6348b40b86a0100001f23deb
