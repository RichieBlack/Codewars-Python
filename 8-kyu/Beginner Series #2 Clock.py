# link: https://www.codewars.com/kata/reviews/56257c742fcbf7eb940000f0/groups/6318e9c5d7d765000112cd5a

def past(h, m, s):
    result = 0
    if s > 0:
        s = s * 1000
    if m > 0:
        m = m * 60000
    if h > 0:
        h = h * 3600000
    result = (s + m + h)
    return result


'''
Best practices
--------------

def past(h, m, s):
    return (3600 * h + 60 * m + s) * 1000

--------------

def past(h, m, s):
    return (s + (m + h * 60) * 60) * 1000

--------------

from datetime import timedelta

def past(h, m, s):
    return timedelta(hours=h, minutes=m, seconds=s) // timedelta(milliseconds=1)

--------------
'''
