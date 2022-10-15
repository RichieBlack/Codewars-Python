# link: https://www.codewars.com/kata/55a75e2d0803fea18f00009d/solutions/python

def find_slope(points):
    a, b, c, d = points

    if a - c == 0:
        return 'undefined'
    else:
        return str(int((b - d) / (a - c)))


# I have been studying Python for two months.

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
