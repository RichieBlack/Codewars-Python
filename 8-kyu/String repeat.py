# link: https://www.codewars.com/kata/reviews/57a98e6aaa22319409000072/groups/57a9cbe2e298a7e22b0003a1

def repeat_str(repeat, string):
    return repeat * string

'''
Best practices
--------------

def repeat_str(repeat, string):
    return repeat * string

--------------

def repeat_str(repeat, string):
    solution = ""
    for i in range(repeat):
        solution += string
    return solution

--------------

repeat_str = lambda r, s: s * r

--------------
'''