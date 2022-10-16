# https://www.codewars.com/kata/reviews/57f2975fb24e723e0e00000a/groups/57f450d7ab9a91ef010002fd

def sum_mix(arr):
    sum = 0
    for i in arr:
        sum += int(i)
    return sum


# I have been studying Python for one month.

"""Best practices
-----------------

def sum_mix(arr):
    return sum(map(int, arr))

-----------------

def sum_mix(arr):
    return sum(int(n) for n in arr)

-----------------

def sum_mix(arr):
    result = 0
    for a in arr:
        try:
            result += a
        except TypeError:
            result += int(a)
    return result

-----------------
"""
