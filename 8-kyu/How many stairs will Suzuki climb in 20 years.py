"""
@File    : How many stairs will Suzuki climb in 20 years.py 
@Author  : Richie Black
@Time    : 27.10.2022 13:55

I have been learning Python since August 2022.
"""


def stairs_in_20(stairs):
    sum_stairs = 0

    for n in range(len(stairs)):
        for i in stairs[n]:
            sum_stairs = sum_stairs + i

    return sum_stairs * 20


"""Best practices
-----------------

def stairs_in_20(stairs):
    return sum(sum(day) for day in stairs) * 20

-----------------

def stairs_in_20(stairs):
    return 20 * sum(map(sum, stairs))

-----------------

def stairs_in_20(stairs):
    tot = 0
    for d in stairs:
        for s in d:
            tot += s
    return tot * 20

-----------------

def stairs_in_20(stairs):
    return sum(sum(stairs, [])) * 20
    
-----------------

stairs_in_20 = lambda _arr: sum(sum(i) for i in _arr) * 20

-----------------
"""

# https://www.codewars.com/kata/reviews/56fcb24936b1139e5700000b/groups/6331ae28ace3020001681288
