"""
@File    : Multiple of index.py 
@Author  : Richie Black
@Time    : 28.10.2022 12:35

I have been learning Python since August 2022.
"""


def multiple_of_index(arr):
    return [arr[i] for i in range(1, len(arr)) if arr[i] % i == 0]


def multiple_of_index_alt(arr):
    new_arr = []

    for i in range(1, len(arr)):
        if arr[i] % i == 0:
            new_arr.append(arr[i])

    return new_arr


"""Best practices
-----------------

def multiple_of_index(l):
    return [l[i] for i in range(1, len(l)) if l[i] % i == 0]

-----------------

def multiple_of_index(arr):
    return [val for index, val in enumerate(arr) if index and val % index == 0]

-----------------

def multiple_of_index(arr):
    i = 1
    rst = []
    while i < len(arr):
        if arr[i] % i == 0:
            print(i)
            rst.append(arr[i])
        i += 1
    return rst

-------------

# https://www.codewars.com/kata/reviews/5a47d66b425057470b00092c/groups/63343ae94c51500001faccb1
