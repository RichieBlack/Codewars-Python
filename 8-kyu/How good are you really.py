# https://www.codewars.com/kata/reviews/5644255cfc3137c889000061/groups/56445976f53bd7b6c700000c

def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)


# I have been studying Python for one month.

"""Best practices
-----------------

def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)

-----------------

def better_than_average(class_points, your_points):
    average = (sum(class_points) + your_points) / (len(class_points) + 1)
    return your_points > average

-----------------

import statistics


def better_than_average(class_points, your_points):
    return your_points > statistics.mean(class_points)

-----------------
"""
