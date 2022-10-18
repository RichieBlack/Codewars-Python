# https://www.codewars.com/kata/reviews/578dc610f50c0d6764000025/groups/632498c71cb1430001b652ec

def sum_array(arr):
    if not arr or len(arr) <= 1:
        return 0

    sort_arr = arr
    sort_arr.sort()
    return (sum(sort_arr[1:-1:]))


# I have been studying Python for one month.

"""Best practices
-----------------

def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)

-----------------

def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr and len(arr) > 1 else 0

-----------------

def sum_array(arr):
    return 0 if arr == None else sum(sorted(arr)[1:-1])

-----------------
"""
