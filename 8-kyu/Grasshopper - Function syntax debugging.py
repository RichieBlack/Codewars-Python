"""
@File    : Grasshopper - Function syntax debugging.py 
@Author  : Richie Black
@Time    : 25.10.2022 19:06

I have been learning Python since August 2022.
"""


def main(verb, noun):
    return verb + noun


"""Best practices
-----------------

def main(verb, noun): 
    return verb + noun

-----------------

def main(verb, noun):
    return f'{verb}{noun}'

-----------------

def main(*a):
    return ''.join(a)

-----------------

main = str.__add__

-----------------
"""

# https://www.codewars.com/kata/reviews/5f2bcecb66c60300016a87ba/groups/632c8173f8f4590001ea98e2
