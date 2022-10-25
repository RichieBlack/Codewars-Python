"""
@File    : The 'if' function.py 
@Author  : Richie Black
@Time    : 25.10.2022 19:28

I have been learning Python since August 2022.
"""


def _if(bool, func1, func2):
    if bool:
        func1()
    else:
        func2()


"""Best practices
-----------------

def _if(bool, func1, func2):
  func1() if bool else func2()

-----------------

def _if(bool, func1, func2):
  if bool:
      func1()
  else:
      func2()

-----------------

_if = lambda b, t, f: (b and t or f)()

-----------------
"""

# https://www.codewars.com/kata/reviews/5446828fef17afd3870001e2/groups/632cd7267db83600014eae1b
