# https://www.codewars.com/kata/reviews/57a5ef88ea0b79d0af00017d/groups/5aeee2c81ac39509a5001975

def distinct(seq):
    return list(dict.fromkeys(seq))


# I have been studying Python for one month.

"""Best practices
-----------------

def distinct(seq):
    return sorted(set(seq), key = seq.index)

-----------------

def distinct(seq):
    result = []
    seen = set()
    for a in seq:
        if a not in seen:
            result.append(a)
            seen.add(a)
    return result

-----------------

def distinct(seq):
    return list(dict.fromkeys(seq))

-----------------
"""
