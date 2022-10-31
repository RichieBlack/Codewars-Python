"""
@File    : Draw stairs.py 
@Author  : Richie Black
@Time    : 31.10.2022 19:17

I have been learning Python since August 2022.
"""


def draw_stairs(n):
    return "".join(" " * i + "I\n" for i in range(n - 1)) + (" " * (n - 1) + "I")


def draw_stairs_alt(n):
    stair = ""

    for i in range(n - 1):
        stair += " " * i + "I\n"

    stair += " " * (n - 1) + "I"

    return stair


"""Best practices
-----------------

def draw_stairs(n):
    return '\n'.join(' ' *i + 'I' for i in range(n))

-----------------

def draw_stairs(n):
  return '\n'.join('I'.rjust(i + 1) for i in range(n))

-----------------

def draw_stairs(n):
    count = 1
    res = ""
    while count < n:
        res += "I\n" + " " * count
        count += 1
    res += "I"
    return res

-----------------
"""

# https://www.codewars.com/kata/reviews/5b4e790409b6d9ee2e003910/groups/635d37992335ef0001ff936b
