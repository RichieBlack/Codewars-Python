def to_jaden_case(string):
    x = string.split()
    n = []

    for i in x:
        n.append(str(i).capitalize())
    return ' '.join(n)

# I have been studying Python for two months.

'''
Best practices
--------------
import string
toJadenCase = string.capwords

--------------
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())
'''