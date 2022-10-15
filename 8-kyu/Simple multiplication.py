# link: https://www.codewars.com/kata/reviews/5b348e41ccc956645000142d/groups/620cc20dfe967e000188ff87

def simple_multiplication(number):
    return number * 8 if number % 2 == 0 else number * 9


# I have been studying Python for one month.

'''
Best practices
--------------

def simple_multiplication(number) :
    return number * 9 if number % 2 else number * 8

--------------

def simple_multiplication(n) :
    return n * (8 + n % 2)

--------------

simple_multiplication = lambda a : a * (8 + (a & 1))

--------------
'''
