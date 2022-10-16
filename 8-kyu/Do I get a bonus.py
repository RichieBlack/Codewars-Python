# https://www.codewars.com/kata/reviews/56f6d91bbf364af086000003/groups/56f7ade03b164cad8f00067d

def bonus_time(salary, bonus):
    if bonus: salary *= 10
    return '$' + str(salary)


# I have been studying Python for one month.

"""
Best practices
--------------

def bonus_time(salary, bonus):
    return "${}".format(salary * (10 if bonus else 1))

--------------

def bonus_time(salary, bonus):
    return '$' + str(salary * [1, 10][bonus])

--------------

bonus_time = lambda salary, bonus: '${}'.format(salary * 10 if bonus else salary) 

--------------
"""
