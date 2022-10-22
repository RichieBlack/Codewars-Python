"""
@File    : Reverse List Order.py 
@Author  : Richie Black
@Time    : 22.10.2022 20:38

I have been learning Python since August 2022.
"""


def reverse_list(list):
    return list[::-1]


"""Best practices
-----------------

def reverse_list(l):
  return l[::-1]

-----------------

def reverse_list(l):
  return list(reversed(l))

-----------------

def reverse_list(l):
  l.reverse()
  return l

-----------------

reverse_list = lambda l: l[::-1]

-----------------
"""
# https://www.codewars.com/kata/reviews/53da6d922a289a768c0018e8/groups/6329c9d7f5f54000010c5702
