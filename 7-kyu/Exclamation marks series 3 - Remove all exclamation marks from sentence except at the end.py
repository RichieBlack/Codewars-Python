"""
@File    : Exclamation marks series 3 - Remove all exclamation marks from sentence except at the end.py 
@Author  : Richie Black
@Time    : 29.10.2022 11:14

I have been learning Python since August 2022.
"""

import re


def remove(s):
    return (
        s.replace('!', '') + ''.join(re.findall('^!+', s[::-1]))
        if s[-1] == '!'
        else s.replace('!', '')
    )


"""Best practices
-----------------

def remove(s):
    return s.replace('!', '') + '!' * (len(s) - len(s.rstrip('!')))

-----------------

import re


def remove(s):
    return re.sub(r'!+(?!!*$)', '', s)

-----------------

def remove(s):
    num = 0
    for letter in s[::-1]:
        if letter != "!":
            break
        num += 1
    return s.replace("!", "") + "!" * num
    
-----------------

def remove(s):
    end_i = len(s.rstrip('!'))
    return s[:end_i].replace('!', '') + s[end_i:]

-----------------
"""

# https://www.codewars.com/kata/reviews/597d2e0bdb26ff9297000021/groups/633f30746a5be2000145baf1
