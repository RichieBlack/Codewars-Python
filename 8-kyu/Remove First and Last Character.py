# link: https://www.codewars.com/kata/reviews/56bf5c369ecef79fc1000076/groups/5834d5af44ff2807d20002bd

def remove_char(s):
    return s[1:-1:]

'''
Best practices
--------------

def remove_char(s):
    return s[1:-1:]

--------------

def remove_char(s):
    return s[1:len(s)-1]

--------------

def remove_char(s):
    return '' if len(s) <= 2 else s[1:-1]

--------------

remove_char = lambda s: s[1:-1]

--------------
'''