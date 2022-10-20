"""
@File    : Correct the mistakes of the character recognition software.py 
@Author  : Richie Black
@Time    : 20.10.2022 20:25

I have been learning Python since August 2022.
"""


def correct(s):
    return s.replace('5', 'S').replace('0', 'O').replace('1', 'I')


def correct_alt(s):
    mistake = {'5': 'S', '0': 'O', '1': 'I'}
    for char in s:
        if char in mistake:
            s = s.replace(char, mistake[char])
    return s


"""Best practices
-----------------

def correct(string):
    return string.translate(str.maketrans("501", "SOI"))

-----------------

def correct(string):
    return string.replace('1', 'I').replace('0', 'O').replace('5', 'S')

-----------------

tr = str.maketrans('015','OIS')

def correct(string):
    return string.translate(tr)

-----------------
"""

# https://www.codewars.com/kata/reviews/57a5d32602f095165700004a/groups/63263b81735d96000116cde3
