# link: https://www.codewars.com/kata/reviews/57e83a3babcee94e1f000071/groups/57e87e8c4ca0e114ad0000dd

def string_to_array(s):
    return s.split(' ')

'''
Best practices
--------------

def string_to_array(string):
    return string.split(" ")

--------------

string_to_array = lambda s: s.split() or [""]

--------------

string_to_array = lambda _: [ __ for __ in _.split(' ')]

--------------
'''