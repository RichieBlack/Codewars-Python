# link: https://www.codewars.com/kata/reviews/571601f0cc5b1c5cd8000020/groups/6309d5caa2f0b000013426c7

def positive_sum(arr):
    sum_pos = 0
    for i in arr:
        if i > 0:
            sum_pos = sum_pos + i
    return sum_pos

'''
Best practices
--------------

def positive_sum(arr):
    return sum(x for x in arr if x > 0)

--------------

def positive_sum(arr):
    return sum(filter(lambda x: x > 0,arr))

--------------

def positive_sum(arr):
    return sum(map(lambda x: x if x > 0 else 0, arr))

--------------
'''