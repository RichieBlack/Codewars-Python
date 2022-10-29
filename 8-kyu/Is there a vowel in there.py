"""
@File    : Is there a vowel in there.py 
@Author  : Richie Black
@Time    : 29.10.2022 11:26

I have been learning Python since August 2022.
"""


def is_vow(inp):
    new = []

    for i in inp:
        if i in [97, 101, 105, 111, 117]:
            new.append(chr(i))
        else:
            new.append(i)
    return new


"""Best practices
-----------------

def is_vow(inp):
    return [chr(n) if chr(n) in "aeiou" else n for n in inp]

-----------------

def is_vow(inp):
    for i, v in enumerate(inp):
        if chr(v) in 'aeiou':
            inp[i] = chr(v)
    return inp

-----------------

def is_vow(s):
    vowels = {97: 'a', 111: 'o', 117: 'u', 101: 'e', 105: 'i'}
    return [vowels.get(a, a) for a in s]

-----------------
"""

# https://www.codewars.com/kata/reviews/57e9241db363405fbc00007b/groups/634066a835b70700015d35b6
