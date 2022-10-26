"""
@File    : Remove First and Last Character Part Two.py 
@Author  : Richie Black
@Time    : 26.10.2022 23:19

I have been learning Python since August 2022.
"""


def array(string):
    string = string.split(',')
    if len(string) < 3:
        return None
    else:
        return ' '.join(string[1:-1])


"""Best practices
-----------------

def array(strng):
    return ' '.join(strng.split(',')[1:-1]) or None

-----------------

def array(string):
  res = ' '.join(string.split(',')[1:-1])
  return res if len(res) > 0 else None

-----------------

def array(string: str):
    return None if not string or len(string.split(',')) <= 2 else ' '.join(string.split(',')[1:-1])

-----------------
"""

# https://www.codewars.com/kata/reviews/57068ad2329356eb64000022/groups/632ea2e9ee1c3f00017f6fd2
