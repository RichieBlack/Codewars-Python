# link: https://www.codewars.com/kata/reviews/53da3de52a289a37bc00128a/groups/53da41e92a289a37bc0012c6

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


'''
Best practices
--------------

def even_or_odd(number):
    return 'Odd' if number % 2 else 'Even'

--------------

def even_or_odd(number):
  return 'Even' if number % 2 == 0 else 'Odd'

--------------

def even_or_odd(number):
  return ["Even", "Odd"][number % 2]

--------------

even_or_odd = lambda number: "Odd" if number % 2 else "Even"

--------------
'''
