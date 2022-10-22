"""
@File    : Regular Ball Super Ball.py 
@Author  : Richie Black
@Time    : 22.10.2022 20:47

I have been learning Python since August 2022.
"""


class Ball(object):
    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type


"""Best practices
-----------------

class Ball(object):
  def __init__(self, type = "regular"):
    self.ball_type = type

-----------------

class Ball(object):
    def __init__(self,ball_type='regular'):
        self.ball_type = ball_type
    def __TomFoolery__(ball_type):
        self.ball_type = "HUGE"

-----------------

class Ball(object):
    def __init__(self, ball_type=None):
        self.ball_type = ball_type or "regular"

-----------------
"""

# https://www.codewars.com/kata/reviews/53f0f96bef9ad427f900012f/groups/632a13a37107960001c77d23
