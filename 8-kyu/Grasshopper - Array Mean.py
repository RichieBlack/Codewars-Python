"""
@File    : Grasshopper - Array Mean.py 
@Author  : Richie Black
@Time    : 27.10.2022 14:20

I have been learning Python since August 2022.
"""


def find_average(nums):
    return sum(nums) / len(nums) if nums else 0


"""Best practices
-----------------

def find_average(nums):
    return float(sum(nums)) / len(nums) if len(nums) !=0 else 0

-----------------

def find_average(nums):
    return sum(nums) / len(nums) if nums else 0

-----------------

import numpy


def find_average(nums):
    return numpy.mean(nums) if nums else 0

-----------------
"""

# https://www.codewars.com/kata/reviews/55dcf04b7776ff9348000004/groups/63336ecf9e58950001261eef
