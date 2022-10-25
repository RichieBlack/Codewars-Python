"""
@File    : Palindrome Strings (retired).py 
@Author  : Richie Black
@Time    : 25.10.2022 19:11

I have been learning Python since August 2022.
"""


def is_palindrome(string):
    string = str(string)
    reverse_string = string[::-1]

    return reverse_string.lower() == string.lower()


"""Best practices
-----------------

def is_palindrome(string):
    return str(string)[::-1] == str(string)

-----------------

def is_palindrome(string):
    return str(string).lower() == str(string).lower()[::-1]

-----------------

is_palindrome = lambda string : str(string) == str(string)[::-1]

-----------------
"""

# https://www.codewars.com/kata/reviews/57aa3a2ed43a6f189600017c/groups/632c89c6f8f4590001ea9ae3
