# https://www.codewars.com/kata/reviews/56b1f01e247c01db92000078/groups/5e1306eae22e9800019f4031

def double_char(s):
    char = ''

    for i in s:
        char += i * 2

    return char


# I have been studying Python for one month.

"""Best practices
-----------------

def double_char(s):
    return ''.join(c * 2 for c in s)

-----------------

def double_char(s):
    res = ''
    for i in s:
        res += i * 2
    return res

-----------------

def double_char(s):
    return ''.join(2 * c for c in s)

-----------------
"""
