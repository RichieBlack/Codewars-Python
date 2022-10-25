"""
@File    : Lario and Muigi Pipe Problem.py 
@Author  : Richie Black
@Time    : 25.10.2022 13:00

I have been learning Python since August 2022.
"""


def pipe_fix(nums):
    return ([n for n in range(nums[0], nums[-1] + 1)])


"""Best practices
-----------------

def pipe_fix(nums):
    return list(range(nums[0], nums[-1] + 1))

-----------------

def pipe_fix(num):
    return range(min(num), max(num) + 1)

-----------------

def pipe_fix(arr):
    ls = []
    for i in range(arr[0],arr[len(arr)-1] + 1):
        ls.append(i)
    return ls

-----------------
"""

# https://www.codewars.com/kata/reviews/56b7fbb90cf562bcaa00001f/groups/632c533bbf0fcc000160d3f5
