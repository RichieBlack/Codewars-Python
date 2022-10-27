"""
@File    : Simple validation of a username with regex.py 
@Author  : Richie Black
@Time    : 27.10.2022 6:55

I have been learning Python since August 2022.
"""


def validate_usr(username):
    chars = 'abcdefghijklmnopqrstuvwxyz1234567890_'
    if 3 < len(username) and len(username) < 17:
        for i in username:
            if i in chars:
                continue
            else:
                return False
        else:
            return True
    return False


"""Best practices
-----------------

import re


def validate_usr(un):
    return re.match('^[a-z0-9_]{4,16}$', un) != None

-----------------

import re


def validate_usr(username):
    return bool(re.match(r'^[a-z0-9_]{4,16}$', username))

-----------------

def validate_usr(username):
    if len(username) < 4 or len(username) > 16:
        return False 
    allowed = 'abcdefghijklmnopqrstuvwxyz0123456789_'
    for i in username:
        if i not in allowed:
            return False
    return True

-----------------

import re


validate_usr = lambda str: bool(re.match('^[a-z\d_]{4,16}$', str))

-----------------
"""

# https://www.codewars.com/kata/reviews/56a6420f333e5367f3000024/groups/632f698456e8d300012fbe5a
