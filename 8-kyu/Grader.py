"""
@File    : Grader.py 
@Author  : Richie Black
@Time    : 29.10.2022 11:57

I have been learning Python since August 2022.
"""


def grader(score):
    if score < 0.6 or score > 1:
        return 'F'
    elif score >= 0.9:
        return 'A'
    elif score >= 0.8:
        return 'B'
    elif score >= 0.7:
        return 'C'
    elif score >= 0.6:
        return 'D'


"""Best practices
-----------------

def grader(x):
    if 0.9 <= x <= 1:
        return "A"
    elif 0.8 <= x < 0.9:
        return "B"
    elif 0.7 <= x < 0.8:
        return "C"
    elif 0.6 <= x < 0.7:
        return "D"
    else:
        return "F"

-----------------

def grader(score):
    for limit, grade in [(0.9, "A"), (0.8, "B"), (0.7, "C"), (0.6, "D")]:
        if limit <= score <= 1:
            return grade
    return 'F'

-----------------

def grader(score):
  return 'F' if score > 1 or score < 0.6 else 'ABCD'[int(10 * (0.999 - score))]

-----------------
"""

# https://www.codewars.com/kata/reviews/53d171d0893164dfbf0010d1/groups/634329ed1ee93e00014ec310
