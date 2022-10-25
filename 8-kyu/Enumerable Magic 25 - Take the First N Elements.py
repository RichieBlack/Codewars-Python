"""
@File    : Enumerable Magic 25 - Take the First N Elements.py 
@Author  : Richie Black
@Time    : 25.10.2022 19:16

I have been learning Python since August 2022.
"""


def take(arr, n):
    return arr[0:n]


"""Best practices
-----------------

def take(arr,n):
    return arr[:n]

-----------------

def take(arr,n):
    arr2 = []
    while n > 0:
        if arr == []:
            break
        arr2.append(arr[0])
        arr.pop(0)
        n -= 1
    return arr2

-----------------

take = lambda arr, n:arr[:n]

-----------------
"""

# https://www.codewars.com/kata/reviews/5d867105a48580000198fc33/groups/632c8be6a2ff6e000162249c
