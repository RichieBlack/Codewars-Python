"""
@File    : Exclamation marks series 6 - Remove n exclamation marks in the sentence from left to right.py 
@Author  : Richie Black
@Time    : 28.10.2022 20:44

I have been learning Python since August 2022.
"""


def remove(s, n):
    list_s = list(s)

    while n > 0:
        if '!' in list_s:
            i = list_s.index('!')
            list_s.pop(i)
        n -= 1

    return (''.join(list_s))


"""Best practices
-----------------

def remove(s, n):
    return s.replace("!", "", n)

-----------------

def remove(s, n):
    liste = []
    k = 1
    for i in range(len(s)):
            if s[i] == "!" and k <= n:
                k += 1
            else:
                liste.append(s[i])
    return "".join(liste)

-----------------

remove = lambda s, n: s.replace('!','',n)

-----------------
"""

# https://www.codewars.com/kata/reviews/580014d3e74d602acc000026/groups/633b127724364f0001dcaec4
