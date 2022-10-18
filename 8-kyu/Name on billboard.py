# https://www.codewars.com/kata/reviews/571f8e386f4aa25e81000051/groups/63237b21362de000011c2052

def billboard(name, price=30):
    total = 0
    count = len(name)
    while count > 0:
        count -= 1
        total += price
    return total


# I have been studying Python for one month.

"""Best practices
-----------------

def billboard(name, price=30):
    return sum(price for letter in name)

-----------------

def billboard(name, price=30):
    cout = 0
    for letters in name:
        cout += price
    return cout

-----------------

def billboard(name, price = 30):
    amt = len(name) / (1.0 / price)
    return amt

-----------------
"""
