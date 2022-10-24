"""
@File    : Find the odd int.py 
@Author  : Richie Black
@Time    : 24.10.2022 19:16

I have been learning Python since August 2022.
"""


def find_it(seq):
    return min([i for i in seq if seq.count(i) % 2])


"""Best practices
-----------------

def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

-----------------

def find_it(seq):
    return [x for x in seq if seq.count(x) % 2][0]

-----------------

import operator


def find_it(xs):
    return reduce(operator.xor, xs)

-----------------

def find_it(seq):
    nums = set()
    for num in seq:
        if num in nums:
            nums.remove(num)
        else:
            nums.add(num)
    return nums.pop()
    
-----------------
"""

# https://www.codewars.com/kata/reviews/56257b3f27e918efed00017c/groups/6356be2157b4a500015c50ca
