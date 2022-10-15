# link: https://www.codewars.com/kata/reviews/545d21e99943f78e6d0000df/groups/629236a5ef20710001d974f4

def string_to_number(s):
    return int(s)


'''
Best practices
--------------

def string_to_number(s):
    return int(s)

--------------

def string_to_number(s):
    try:
        return int(s)
    except (ValueError):
        return "Input is not valid "

--------------

string_to_number = int

--------------

string_to_number = lambda n: int(n)

--------------
'''