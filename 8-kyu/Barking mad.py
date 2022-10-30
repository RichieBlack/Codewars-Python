"""
@File    : Barking mad.py 
@Author  : Richie Black
@Time    : 30.10.2022 14:23

I have been learning Python since August 2022.
"""


class Dog:
    def __init__(self, breed):
        self.breed = breed


snoopy = Dog("Beagle")

snoopy.bark = lambda: "Woof"

scoobydoo = Dog("Great Dane")

scoobydoo.bark = lambda: "Woof"

"""Best practices
-----------------

class Dog ():
  def __init__(self, breed):
    self.breed = breed
  def bark(self):
    return "Woof"

snoopy = Dog("Beagle")

scoobydoo = Dog("Great Dane")

-----------------

class Dog ():
  def __init__(self, breed):
    self.breed = breed
    self.bark = lambda: "Woof"
    
snoopy = Dog("Beagle")

scoobydoo = Dog("Great Dane")

-----------------

class Dog ():
  def __init__(self, breed):
    self.breed = breed
    

snoopy = Dog("Beagle")

snoopy.bark = lambda: "Woof"

scoobydoo = Dog("Great Dane")

scoobydoo.bark = lambda: "Woof"

-----------------
"""

# https://www.codewars.com/kata/reviews/553a86f91e039900d6000162/groups/634345eb42231700011ebe40
