# https://www.codewars.com/kata/reviews/56473f00617b6354650000d4/groups/56477759ccf79c920a0000ad

def get_average(marks):
    return int(sum(marks) / len(marks))


# I have been studying Python for one month.

"""Best practices
-----------------

def get_average(marks):
    return sum(marks) // len(marks)

-----------------

import numpy


def get_average(marks):
    return int(numpy.mean(marks))

-----------------

def get_average(marks):
    return sum(marks) / len(marks)

-----------------
"""
