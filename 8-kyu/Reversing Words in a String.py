"""
@File    : Reversing Words in a String.py 
@Author  : Richie Black
@Time    : 26.10.2022 23:14

I have been learning Python since August 2022.
"""


def reverse(string):
    return ' '.join(reversed(string.split()))


"""Best practices
-----------------

def reverse(st):
    return " ".join(reversed(st.split())).strip()

-----------------

def reverse(st):
    st = st.split()
    st.reverse()
    return ' '.join(st)

-----------------

reverse = lambda n: ' '.join(filter(bool, n.strip().split(' ')[::-1]))

-----------------
"""

# https://www.codewars.com/kata/reviews/57a7772702f095ae6d00017c/groups/632e0eb3ee1c3f00017f5a09
