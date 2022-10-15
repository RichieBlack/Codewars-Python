# link: https://www.codewars.com/kata/reviews/55246c58de8b4bcd960003a1/groups/6317c6e70c7ef00001d077a1

def square_sum(numbers):
    square = []
    result = 0

    for i in numbers:
        square.append(i * i)

    for i in square:
        result += i

    return result


'''
Best practices
--------------

def square_sum(numbers):
    return sum(x ** 2 for x in numbers)

--------------

def square_sum(numbers):
    return sum(map(lambda x: x ** 2, numbers))

--------------

import numpy

def square_sum(numbers):
    return sum(numpy.array(numbers) ** 2)

--------------

square_sum = lambda n: sum(e ** 2 for e in n)

--------------
'''