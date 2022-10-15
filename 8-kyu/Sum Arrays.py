# link: https://www.codewars.com/kata/reviews/54cd6ef118cae04721000085/groups/5bb48c03484fcd66c2000748

def sum_array(a):
    sum = 0
    for i in a:
        sum += i
    return sum


'''
Best practices
--------------

def sum_array(a):
  return sum(a)

--------------

def sum_array(a):
    return sum(a) if a else 0

--------------

def sum_array(a):
    sum = 0
    for i in a:
        sum += i
    return sum

--------------

sum_array = sum

--------------

sum_array = lambda a: sum(a)

--------------
'''
