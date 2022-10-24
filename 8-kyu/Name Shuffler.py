"""
@File    : Name Shuffler.py 
@Author  : Richie Black
@Time    : 24.10.2022 22:38

I have been learning Python since August 2022.
"""


def name_shuffler(string):
    return ' '.join(string.split()[::-1])


"""Best practices
-----------------

def name_shuffler(str_):
    return ' '.join(str_.split(' ')[::-1])

-----------------

def name_shuffler(str_):
    [first, last] = str_.split()
    return last + " " + first

-----------------

def name_shuffler(s):
    return ' '.join(reversed(s.split()))

-----------------
"""

# https://www.codewars.com/kata/reviews/559d176593c2ebe903000097/groups/632b0ff00f851c0001736360
