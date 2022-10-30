"""
@File    : ASCII Total.py
@Author  : Richie Black
@Time    : 26.10.2022 22:57

I have been learning Python since August 2022.
"""


def uni_total(s):
    sum_chars = []

    for i in list(s):
        sum_chars.append(ord(i))

    return sum(sum_chars)


'''
Best practices
--------------
def uni_total(string):
    return sum(map(ord, string))

--------------

def uni_total(s):
    return sum(ord(c) for c in s)

--------------
'''

# https://www.codewars.com/kata/reviews/572cfec7a321a296a3000058/groups/6346b4737b911e0001bc6a9b
