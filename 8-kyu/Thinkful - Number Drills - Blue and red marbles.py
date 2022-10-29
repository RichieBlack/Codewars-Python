"""
@File    : Thinkful - Number Drills - Blue and red marbles.py 
@Author  : Richie Black
@Time    : 29.10.2022 11:24

I have been learning Python since August 2022.
"""


def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    return ((blue_start - blue_pulled) / ((blue_start - blue_pulled) + (red_start - red_pulled)))


"""Best practices
-----------------

def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    blue_remaining = blue_start - blue_pulled
    red_remaining = red_start - red_pulled
    return blue_remaining / (blue_remaining + red_remaining)

-----------------

def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    return (blue_start - blue_pulled)/((red_start - red_pulled)+(blue_start - blue_pulled))

-----------------

guess_blue = lambda bs, rs, bp, rp: (bs - bp) / (bs + rs - bp - rp)

-----------------
"""

# https://www.codewars.com/kata/reviews/5862f66bf5ac2b1ba3000f46/groups/633ffc1ce117d500010c1e4a
