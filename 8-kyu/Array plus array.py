# link: https://www.codewars.com/kata/reviews/5a4b8fb4a808393510000f58/groups/5a4cad08cb35292bf70019b5

def array_plus_array(arr1, arr2):
    sum1 = 0
    sum2 = 0

    for i in arr1:
        sum1 += i

    for i in arr2:
        sum2 += i

    return sum1 + sum2

# I have been studying Python for one month.

'''
Best practices
--------------

def array_plus_array(arr1,arr2):
    return sum(arr1+arr2)

--------------

def array_plus_array(arr1,arr2):
    return sum(arr1) + sum(arr2)

--------------

array_plus_array = lambda a, b: sum(a + b)

--------------
'''