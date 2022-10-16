# https://www.codewars.com/kata/reviews/552253df667a8dbf7600045b/groups/55286b8a040e357018000a6d

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)


# I have been studying Python for one month.

"""
---------------
Best practices
---------------

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name = name)

---------------

def greet(name):
    return "Hello, {name}!".format(name=('my love' if name == 'Johnny' else name));

---------------

greet = lambda name: "Hello, " + ("my love" if name == "Johnny" else name) + "!"

---------------
"""
