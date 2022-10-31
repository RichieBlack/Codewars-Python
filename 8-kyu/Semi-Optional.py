"""
@File    : Semi-Optional.py 
@Author  : Richie Black
@Time    : 31.10.2022 18:44

I have been learning Python since August 2022.
"""


def wrap(value):
    return {"value": value}


"""Best practices
-----------------

def wrap(value):
    return {"value": value}

-----------------

class wrap:
    def __init__(self,value,key="value"):
        self.__value = value
        self.__key = key
    def __getitem__(self,key):
        if self.__key == key:
            return self.__value
        raise KeyError("Your key", key,"is incorrect")

-----------------

wrap = lambda value:{"value": value}

-----------------
"""

# https://www.codewars.com/kata/reviews/622cdd06d6ee15000166511c/groups/634f2675cc8e290001ede0ac
