# https://www.codewars.com/kata/reviews/58b1822cb6c10592d9000ccb/groups/6210fde9cf0a220001821f90

def seats_in_theater(tot_cols, tot_rows, col, row):
    return (tot_cols - col + 1) * (tot_rows - row)


# I have been studying Python for one month.

"""Best practices
-----------------

def seats_in_theater(tot_cols, tot_rows, col, row):
    return (tot_cols - col + 1) * (tot_rows - row)

-----------------

import numpy as np


def seats_in_theater(tot_cols, tot_rows, col, row):
    matrix = np.array([[tot_cols, tot_rows], [col - 1, row]])
    r = matrix[0] - matrix[1]
    return r[0] * r[1]

-----------------

seats_in_theater = lambda tc, tr, c, r: (tc - c + 1) * (tr - r)

-----------------
"""
