"""
@File    : 101 Dalmatians - squash the bugs, not the dogs.py 
@Author  : Richie Black
@Time    : 25.10.2022 19:08

I have been learning Python since August 2022.
"""


def how_many_dalmatians(number):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    respond = []

    if number <= 10:
        respond = dogs[0]
    elif number <= 50:
        respond = dogs[1]
    elif number == 101:
        respond = dogs[3]
    else:
        respond = dogs[2]
    return respond


"""Best practices
-----------------

def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    return dogs[0] if n <= 10 else dogs[1] if n <= 50 else dogs[3] if n == 101 else dogs[2]

-----------------

def how_many_dalmatians(n):
  dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
  
  if n <= 10:
      return dogs[0]
  elif n <= 50:
      return dogs[1]
  elif n < 101:
      return dogs[2] 
  else:
      return dogs[3]

-----------------

responses = [
  (lambda n: n < 11, "Hardly any"), 
  (lambda n: n < 51, "More than a handful!"), 
  (lambda n: n == 101, "101 DALMATIONS!!!"),
  (lambda n: True, "Woah that's a lot of dogs!")
]

how_many_dalmatians = lambda n: next(r for p, r in responses if p(n))

-----------------
"""

# https://www.codewars.com/kata/reviews/56f6b7cd9b6590d2d80000e8/groups/632c8484f8f4590001ea9979
