"""
@File    : Surface Area and Volume of a Box.py 
@Author  : Richie Black
@Time    : 20.10.2022 20:55

I have been learning Python since August 2022.
"""


def get_size(w, h, d):
    result = []
    area = 2 * (w * h + w * d + h * d)
    volume = w * h * d
    result.append(area)
    result.append(volume)
    return result


"""Best practices
-----------------

def get_size(w, h, d):
    area = 2 * (w*h + h*d + w*d)
    volume = w * h * d
    return [area, volume]

-----------------

def get_size(w, h, d):
    return [2 * (w*d + h*d + h*w), w * h * d]

-----------------

get_size = lambda w, h, d: [w*h*2 + w*d*2 + h*d*2, w * h * d]

-----------------
"""

# https://www.codewars.com/kata/reviews/565f87526b95b4d67800001d/groups/6328445e6f58be00018e99bb
