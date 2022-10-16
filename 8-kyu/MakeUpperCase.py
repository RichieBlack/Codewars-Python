# https://www.codewars.com/kata/reviews/599c92f7aa791154c2002da3/groups/599c9502aa791165b1002dca

def make_upper_case(s): return s.upper()


# I have been studying Python for one month.

"""
---------------
Best practices
---------------

def make_upper_case(s): return s.upper()

---------------

make_upper_case = str.upper

---------------

def make_upper_case(s):
    return ''.join(chr(ord(ch) - 32) if ord(ch) in range(97, 123) else ch for ch in s)

---------------
"""