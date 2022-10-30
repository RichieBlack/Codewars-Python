"""
@File    : How do I compare numbers.py
@Author  : Richie Black
@Time    : 25.10.2022 12:37

I have been learning Python since August 2022.
"""


def what_is(x):
    if x == 42:
        return 'everything'
    elif x == 42 * 42:
        return 'everything squared'
    else:
        return 'nothing'


'''
Best practices
--------------

def what_is(x):
    if x == 42:
        return 'everything'
    elif x == 42 * 42:
        return 'everything squared'
    else:
        return 'nothing'

--------------

def what_is(x):
  return { 42: 'everything', 1764: 'everything squared' }.get(x, 'nothing')

--------------
'''

# https://www.codewars.com/kata/reviews/55d892d3ce5342c518000107/groups/63474f0ca212a80001898172
