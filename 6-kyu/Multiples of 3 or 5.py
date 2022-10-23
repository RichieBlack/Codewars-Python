"""
@File    : Multiples of 3 or 5.py 
@Author  : Richie Black
@Time    : 23.10.2022 21:27

I have been learning Python since August 2022.
"""


def solution(number):
    return sum([n for n in range(1, number) if n % 3 == 0 or n % 5 == 0])


"""Best practices
-----------------

def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

-----------------

def solution(number):
    sum = 0
    for i in range(number):
        if (i % 3) == 0 or (i % 5) == 0:
            sum += i
    return sum

-----------------

def solution(number):
    a3 = (number-1)/3
    a5 = (number-1)/5
    a15 = (number-1)/15
    result = (a3*(a3+1)/2)*3 + (a5*(a5+1)/2)*5 - (a15*(a15+1)/2)*15
    return result

-----------------

def solution(number):
    threes = range(3, number, 3)
    fives = range(5, number, 5)
    return sum(list(set(threes + fives)))

-----------------
"""

# https://www.codewars.com/kata/reviews/54a5ebd237f4350faf00006c/groups/63557e8907f007000186dff5
