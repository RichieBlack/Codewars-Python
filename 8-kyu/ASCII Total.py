def uni_total(s):
    sum_chars = []

    for i in list(s):
        sum_chars.append(ord(i))

    return sum(sum_chars)

# I have been studying Python for two months.

'''
Best practices
--------------
def uni_total(string):
    return sum(map(ord, string))

--------------

def uni_total(s):
    return sum(ord(c) for c in s)

--------------
'''