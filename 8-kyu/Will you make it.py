# https://www.codewars.com/kata/reviews/5861d292124b35723e000060/groups/5a4128df6d95dfd6bc001d14

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return fuel_left >= distance_to_pump / mpg


# I have been studying Python for one month.

"""Best practices
-----------------

def zeroFuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left

-----------------

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if fuel_left >= distance_to_pump / mpg:
        return True
    else:
        return False

-----------------

zero_fuel = lambda d, m, f : d <= m * f

-----------------
"""
