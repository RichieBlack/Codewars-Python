"""
@File    : Basic subclasses - Adam and Eve.py 
@Author  : Richie Black
@Time    : 30.10.2022 23:33

I have been learning Python since August 2022.
"""


def God():
    return Man(), Woman()


class Human:
    def human(self):
        pass


class Man(Human):
    pass


class Woman(Human):
    pass


"""Best practices
-----------------

def God():
    return [Man(), Woman()]

class Human(object):
    pass

class Man(Human):
    pass
    
class Woman(Human):
    pass

-----------------

class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    return [Man(), Woman()]

-----------------

def God():
  return [Man(), Woman()]

class Human:
  def __init__(self):
    pass

class Man(Human):
  def __init__(self):
    pass

class Woman(Human):
  def __init__(self):
    pass

-----------------
"""

# https://www.codewars.com/kata/reviews/547c58dc2269c8502a000031/groups/634eb9cceca9f5000189d5a9
