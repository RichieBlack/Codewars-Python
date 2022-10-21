"""
@File    : Find numbers which are divisible by given number.py 
@Author  : Richie Black
@Time    : 21.10.2022 21:48

I have been learning Python since August 2022.
"""


def divisible_by(numbers, divisor):
    return [i for i in numbers if not i % divisor]


"""Best practices
-----------------

def divisible_by(numbers, divisor):
    return [x for x in numbers if x % divisor == 0]

-----------------

def divisible_by(numbers, divisor):
    div_by = []
    for num in numbers:
        if num % divisor == 0:
            div_by.append(num)
    return div_by

-----------------

def divisible_by(n, d):
    return list(filter(lambda x: not x % d, n))

-----------------
"""

# https://www.codewars.com/kata/reviews/565f43beb889334aed00010a/groups/6329b92a7194040001d4d480
