# link: https://www.codewars.com/kata/reviews/61b89ede29ac8e0001eb6188/groups/61cb19fd7269000001ed8407

def same_case(a, b):
    if not (a.isalpha() and b.isalpha()):
        return -1

    if (a.islower() and b.islower()) or (a.isupper() and b.isupper()):
        return 1
    else:
        return 0

# I have been studying Python for one month.

'''
Best practices
--------------

def same_case(a, b):
    return a.isupper() == b.isupper() if a.isalpha() and b.isalpha() else -1

--------------

def same_case(a, b):
    if a.isalpha() and b.isalpha():
        if (a.islower() and b.islower()) or (a.isupper() and b.isupper()):
            return 1
        else:
            return 0
    else:
        return -1

--------------

def same_case(a, b):
    c = a+b
    if not c.isalpha():
        return -1
    if c.islower() or c.isupper():
        return 1
    else:
        return 0

--------------

same_case = lambda *C: not all(c.isalpha() for c in C) and -1 or all(c.isupper() for c in C) or all(c.islower() for c in C)

--------------

from string import ascii_letters as c

same_case = lambda a, b: a.isupper() == b.isupper() if a in c and b in c else -1

--------------
'''