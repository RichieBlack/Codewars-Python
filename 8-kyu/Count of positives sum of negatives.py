# https://www.codewars.com/kata/reviews/5794a7cb1051be2d9c000016/groups/631cbc718b0bcd0001041a2b

def count_positives_sum_negatives(arr):
    pos = 0
    neg = 0
    for i in arr:
        if i > 0:
            pos += 1
        if i < 0:
            neg += i
    if not arr:
        return []
    return [pos, neg]


# I have been studying Python for one month.

"""
---------------
Best practices
---------------

def count_positives_sum_negatives(arr):
    if not arr: return []
    pos = 0
    neg = 0
    for x in arr:
      if x > 0:
          pos += 1
      if x < 0:
          neg += x
    return [pos, neg]

---------------

def count_positives_sum_negatives(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []

---------------

def count_positives_sum_negatives(arr):
    return [len([x for x in arr if x > 0])] + [sum(y for y in arr if y < 0)] if arr else []

---------------
"""
