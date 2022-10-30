"""
@File    : Fuel Calculator.py 
@Author  : Richie Black
@Time    : 30.10.2022 23:44

I have been learning Python since August 2022.
"""


def fuel_price2(litres, price_per_litre):
    discount_values = {2: 0.05, 3: 0.05, 4: 0.1, 5: 0.1, 6: 0.15, 7: 0.15, 8: 0.2, 9: 0.2}

    if litres in discount_values:
        index = litres
        return round(litres * (price_per_litre - discount_values[index]), 2)
    else:
        return round(litres * (price_per_litre - 0.25), 2)


def fuel_price_alt(litres, price_per_litre):
    discount = 0

    if 1 < litres < 4:
        discount = 0.05

    if 3 < litres < 6:
        discount = 0.1

    if 5 < litres < 8:
        discount = 0.15

    if 7 < litres < 10:
        discount = 0.2

    if litres >= 10:
        discount = 0.25

    return round(litres * (price_per_litre - discount), 2)


"""Best practices
-----------------

def fuel_price(litres, price_per_liter):
    discount = int(min(litres, 10)/2) * 5 / 100
    return round((price_per_liter - discount) * litres, 2)


-----------------

def fuel_price(litres, price_per_liter):
    
    discount = (litres // 2) * 0.05
    if litres >= 10:
        discount = 0.25
    
    total = round((price_per_liter - discount) * litres,2)
    
    return total

-----------------

fuel_price = lambda l, p: round(l * (p - min(0.05 * (l // 2), 0.25)), 2)

-----------------
"""

# https://www.codewars.com/kata/reviews/57b5f4c88a36ac1d46000fae/groups/634edad2cc8e290001edd104
