"""
@File    : Exclamation marks series 1 - Remove an exclamation mark from the end of string.py 
@Author  : Richie Black
@Time    : 26.10.2022 23:24

I have been learning Python since August 2022.
"""


def remove(s):
    if s == '': return ''
    if s[-1] == '!':
        s = list(s)
        s.pop(-1)
    return ''.join(s)


"""Best practices
-----------------

def remove(s):
    return s[:-1] if s.endswith('!') else s

-----------------

def remove(s):
    return s[:-1] if s and s[-1] == '!' else s

-----------------

import re
    
    
def remove(s):
    return re.sub(r'!$', '', s)

-----------------

def remove(s):
    if s.endswith("!"):
        s = s[:-1] 
    return s
    
-----------------
"""

# https://www.codewars.com/kata/reviews/5800161fe74d60d4d4000029/groups/632ed04b7ca3450001b006d6
