"""
@File    : Find the Slope.py
@Author  : Richie Black
@Time    : 26.10.2022 20:47

I have been learning Python since August 2022.
"""


def find_slope(points):
    a, b, c, d = points

    if a - c == 0:
        return 'undefined'
    else:
        return str(int((b - d) / (a - c)))


'''
Best practices
--------------

def find_slope(points):
    try:
        return str((points[3]-points[1])/(points[2]-points[0]))
    except ZeroDivisionError:
        return "undefined"

--------------

def find_slope(points):
    x1, y1, x2, y2 = points
    return 'undefined' if x1 == x2 else (y2 - y1) / (x2 - x1)

--------------
'''

# https://www.codewars.com/kata/reviews/55dbedf7865e93737400000e/groups/63465cbf8c27ed00016ffd6b
