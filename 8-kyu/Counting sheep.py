# https://www.codewars.com/kata/reviews/550af10c9c1f8949220001f9/groups/620f9f18af59b5000126126f

def count_sheeps(sheep):
    result = 0

    for i in sheep:
        if i:
            result += 1
    return result


# I have been studying Python for one month.

"""
---------------
Best practices
---------------

def count_sheeps(arrayOfSheeps):
  return arrayOfSheeps.count(True)

---------------

def count_sheeps(array_of_sheep):
  count = 0
  for sheep in array_of_sheep:
      if sheep:
          count += 1
  return count

---------------

def count_sheeps(x):
  return x.count(True)

---------------

def count_sheeps(sheep):
  return len([x for x in sheep if x])

---------------
"""
