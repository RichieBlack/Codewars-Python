# https://www.codewars.com/kata/reviews/5865756e02698c83e60006d8/groups/5cb76fa0b43a5100010945b3

def find_average(numbers):
   return sum(numbers) / len(numbers)


# I have been studying Python for one month.

"""
---------------
Best practices
---------------

def find_average(array):
    return sum(array) / len(array) if array else 0

---------------

def find_average(numbers):
   return sum(numbers) / len(numbers)

---------------

def find_average(array):
    try:
        return sum(array) / len(array)
    except ZeroDivisionError:
        return 0

---------------

from statistics import mean as find_average

---------------
"""