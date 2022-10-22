"""
@File    : Find the capitals.py 
@Author  : Richie Black
@Time    : 22.10.2022 20:36

I have been learning Python since August 2022.
"""


def capitals(word):
    word_Upper = word.upper()
    count_Caps = []

    for i in range(len(word)):
        if word[i] == word_Upper[i]:
            count_Caps += [i]
    return count_Caps


"""Best practices
-----------------

def capitals(word):
    return [i for (i, c) in enumerate(word) if c.isupper()]

-----------------

def capitals(word):
    uppers = []
    for i in range(len(word)):
        if word[i].isupper():
            uppers.append(i)
    return uppers

-----------------

def capitals(word):
    return [i for i in range(len(word)) if word[i].isupper()]

-----------------

def capitals(word):
    return filter(lambda x: word[x].isupper(), range(len(word)))

-----------------
"""

# https://www.codewars.com/kata/reviews/54ff96a8c50295d59d000615/groups/6329c7ef7107960001c768ad
