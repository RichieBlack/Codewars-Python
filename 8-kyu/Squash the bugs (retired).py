"""
@File    : Squash the bugs (retired).py 
@Author  : Richie Black
@Time    : 22.10.2022 21:07

I have been learning Python since August 2022.
"""


def find_longest(string):
    spl = string.split(" ")
    longest = 0
    i = 0

    while (i < len(spl)):
        if (len(spl[i]) > longest):
            longest = len(spl[i])
            i += 1
        else:
            i += 1
    return longest


"""Best practices
-----------------

def find_longest(strng):
    return max(len(a) for a in strng.split())

-----------------

def find_longest(string):
    return max(map(len, string.split()))

-----------------

def find_longest(string):
    spl = string.split(" ")
    longest = 0
    i=0
    while (i < len(spl)):
        print(spl[i])
        if (len(spl[i]) > longest):
            longest = len(spl[i])
        i +=1
    return longest

-----------------
"""

# https://www.codewars.com/kata/reviews/56f7d4c38abc385c18000002/groups/632a34f33c54090001dab006
