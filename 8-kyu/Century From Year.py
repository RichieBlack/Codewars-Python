# link: https://www.codewars.com/kata/reviews/5a4a56c7a7c21c42b0000350/groups/5a4a56c7dbcf4104f0000257

def century(year):
    return (year + 99) // 100


'''
Best practices
--------------

def century(year):
    return (year + 99) // 100

--------------

import math

def century(year):
    return math.ceil(year / 100)

--------------

def century(year):
    return (year / 100) if year % 100 == 0 else year // 100 + 1

--------------

century = lambda y: (y + 99) // 100

--------------
'''
