"""
@File    : Grasshopper - Debug.py 
@Author  : Richie Black
@Time    : 25.10.2022 19:01

I have been learning Python since August 2022.
"""


def weather_info(temp):
    c = (temp - 32) * (5 / 9)
    if (c < 0):
        return (f"{c} is freezing temperature")
    else:
        return (f"{c} is above freezing temperature")


"""Best practices
-----------------

def weather_info (temp):
    c = convertToCelsius(temp)
    if (c <= 0):
        return (str(c) + " is freezing temperature")
    else:
        return (str(c) + " is above freezing temperature")
    
def convertToCelsius (temperature):
  celsius = (temperature - 32) * (5.0 / 9.0)
  return celsius

-----------------

def weather_info (t):
  c = (t - 32) * (5.0 /9)
  return str(c) + " is freezing temperature" if c <= 0 else str(c) + " is above freezing temperature"


-----------------

def weather_info(fahrenheit):
    celsius = 5.0 * (fahrenheit - 32) / 9
    return "{} is {}freezing temperature".format(celsius, "above " if celsius >= 0 else "")

-----------------
"""

# https://www.codewars.com/kata/reviews/5623ccd5762213e8dc0000c4/groups/632c7f39f8f4590001ea9826
