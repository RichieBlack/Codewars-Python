"""
@File    : Grasshopper - Terminal Game 1.py 
@Author  : Richie Black
@Time    : 28.11.2022 1:26

I have been learning Python since August 2022.
"""


class Hero(object):
    def __init__(self, name='Hero'):
        self.name = name
        self.position = '00'
        self.health = 100
        self.damage = 5
        self.experience = 0


myHero = Hero()

"""Best practices
-----------------

class Hero(object):
    def __init__(self, name='Hero'):
        self.name = name
        self.position = '00'
        self.health = 100
        self.damage = 5
        self.experience = 0

-----------------

class Hero(object):
    def __init__(self, name="Hero", position="00",
                health=100, damage=5, experience=0):
        self.name = name
        self.position = position
        self.max_health = health #trust me, you want to have this as well
        self.health = health 
        self.damage = damage
        self.experience = experience

-----------------

class Hero(object):
  def __init__(self, name = 'Hero'):
    self.name, self.position, self.health, self.damage, self.experience = name, '00', 100, 5, 0

-----------------
"""

# https://www.codewars.com/kata/reviews/55f59bf7a47947a7270000a7/groups/6383d62dc53d4600010e1594
