"""
@File    : Sum of differences in array.py 
@Author  : Richie Black
@Time    : 27.10.2022 14:05

I have been learning Python since August 2022.
"""


def sum_of_differences(arr):
    arr_sort = sorted(arr)
    arr_sort.reverse()
    sum = 0

    for i in range(len(arr) - 1):
        sum += arr_sort[i] - arr_sort[i + 1]

    return sum


"""Best practices
-----------------

def sum_of_differences(arr):
    return max(arr) - min(arr) if arr else 0

-----------------

def sum_of_differences(arr):
    arr.sort(reverse=True)
    i = 0
    res = 0
    while i < len(arr)-1:
        res += arr[i] - arr[i+1]
        i += 1
    return res

-----------------

def sum_of_differences(arr):
    arr = sorted(arr, reverse=True)
    return sum(a - b for a, b in zip(arr, arr[1:]))

-----------------
"""

# https://www.codewars.com/kata/reviews/628b6bc36a07770001d1489d/groups/6332c5691e72e00001cb00ac
