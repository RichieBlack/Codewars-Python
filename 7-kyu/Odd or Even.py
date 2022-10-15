# link: https://www.codewars.com/kata/reviews/5a2c002b57de08b5a8000f47/groups/5e3d369c99d28600018f24f2

def odd_or_even(arr):
    sum = 0
    for i in arr:
        sum += i
    if sum % 2 == 0:
       return "even"
    else:
       return "odd"


'''
Best practices
--------------

def oddOrEven(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'

--------------

def oddOrEven(arr):
    return ('even', 'odd')[sum(arr) % 2]

--------------

oddOrEven = lambda x: "odd" if sum(x) % 2 else "even"

--------------
'''