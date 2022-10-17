# https://www.codewars.com/kata/reviews/58091aa1d6c9564526000038/groups/586fc021618362d54d000f4e

def fake_bin(x):
    bin = ""
    for i in x:
        if int(i) < 5:
            bin += "0"
        else:
            bin += "1"
    return bin


# I have been studying Python for one month.

"""Best practices
-----------------

def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)

-----------------

def fake_bin(x):
    result = ""
    for num in x:
        if int(num) < 5:
            result = result + "0"
        else:
            result = result + "1"
    return result

-----------------

import string


def fake_bin(s):
    return s.translate(string.maketrans('0123456789', '0000011111'))

-----------------
"""
