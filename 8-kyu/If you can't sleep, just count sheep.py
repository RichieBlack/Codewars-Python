# https://www.codewars.com/kata/reviews/5b3fcb04fec6700205000299/groups/5c608539d40a5d00017a1af7

def count_sheep(n):
    sheep = ""
    for i in range(n):
        sheep += f"{i + 1} sheep..."
    return sheep


# I have been studying Python for one month.

"""Best practices
-----------------

def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1, n + 1))

-----------------

def count_sheep(n):
    sheep=""
    for i in range(1, n + 1):
        sheep+=str(i) + " sheep..."
    return sheep

-----------------

def count_sheep(n):
    return "".join("{} sheep...".format(i) for i in range(1, n + 1))

-----------------
"""
