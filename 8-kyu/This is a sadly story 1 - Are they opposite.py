"""
@File    : This is a sadly story 1 - Are they opposite.py 
@Author  : Richie Black
@Time    : 31.10.2022 19:04

I have been learning Python since August 2022.
"""


def is_opposite(s1, s2):
    check_char = []

    if s1 == "" or s2 == "":
        return False

    for i in range(len(s1)):

        if ord(s1[i]) - 32 == ord(s2[i]):
            check_char.append(1)

        elif ord(s1[i]) + 32 == ord(s2[i]):
            check_char.append(1)

        else:
            check_char.append(0)

    return 0 not in check_char


"""Best practices
-----------------

def is_opposite(s1, s2):
    return False if not(s1 or s2) else s1.swapcase() == s2

-----------------

def is_opposite(s1,s2):
    return s1 != "" and s1.swapcase() == s2

-----------------

def is_opposite(s1,s2):
    return s1 == s2.swapcase() if s1 else False

-----------------

def is_opposite(s1, s2):
    return bool(s1) and s1.swapcase() == s2
    
-----------------
"""

# https://www.codewars.com/kata/reviews/57a009dd8ac8e7aaac0000b3/groups/63530e85035e3600012d62cd
