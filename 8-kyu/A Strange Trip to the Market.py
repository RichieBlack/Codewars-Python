"""
@File    : A Strange Trip to the Market.py 
@Author  : Richie Black
@Time    : 28.10.2022 20:32

I have been learning Python since August 2022.
"""


def is_lock_ness_monster(string):
    return any(tree_fiddy in string for tree_fiddy in ('tree fiddy', 'three fifty', '3.50'))


"""Best practices
-----------------

def is_lock_ness_monster(s):
    return any(i in s for i in ('tree fiddy', 'three fifty', '3.50'))

-----------------

import re


def is_lock_ness_monster(s):
    return bool(re.search(r"3\.50|tree fiddy|three fifty", s))

-----------------

def is_lock_ness_monster(s):
    return any(map(lambda x:x in s, ('tree fiddy','three fifty','3.50')))

-----------------
"""

# https://www.codewars.com/kata/reviews/5c3e9a5ea4a1490001076a03/groups/6337027eb4bbdf000141e931
