"""
@File    : Find the Difference in Age between Oldest and Youngest Family Members.py 
@Author  : Richie Black
@Time    : 27.10.2022 14:34

I have been learning Python since August 2022.
"""


def difference_in_ages(ages):
    return (min(ages), max(ages), max(ages) - min(ages))


"""Best practices
-----------------

def difference_in_ages(ages):
    return (min(ages) , max(ages) , max(ages) - min(ages))

-----------------

def difference_in_ages(ages):
    x, y = min(ages), max(ages)
    return x, y, y-x

-----------------

def difference_in_ages(ages):
    age = sorted(ages)
    return (age[0], age[-1], (age[-1] - age[0]))

-----------------
"""

# https://www.codewars.com/kata/reviews/5e720f5fa67bfb00013f35e3/groups/6334322ccca62a0001602b41
