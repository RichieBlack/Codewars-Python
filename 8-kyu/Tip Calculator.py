"""
@File    : Tip Calculator.py 
@Author  : Richie Black
@Time    : 29.10.2022 0:50

I have been learning Python since August 2022.
"""

import math


def calculate_tip(amount, rating):
    ratings = {
        'terrible': 0,
        'poor': 0.05,
        'good': 0.1,
        'great': 0.15,
        'excellent': 0.2
    }

    if rating.lower() in ratings:
        return math.ceil(amount * ratings.get(rating.lower()))
    else:
        return 'Rating not recognised'


"""Best practices
-----------------

from math import ceil


def calculate_tip(amount, rating):
    tips = {
        'terrible': 0,
        'poor' : .05,
        'good' : .1,
        'great' : .15,
        'excellent' : .2
    }
    if rating.lower() in tips:
        return ceil(amount * tips[rating.lower()])
    else:
        return 'Rating not recognised'

-----------------

import math


def calculate_tip(amount, rating):
    tipTypes = ["terrible","poor","good","great","excellent"]
    
    if rating.lower() in tipTypes:
        return math.ceil(amount * tipTypes.index(rating.lower()) * 0.05)
    else: 
        return "Rating not recognised"

-----------------

import math


def calculate_tip(a, r):
    return {"terrible": 0 * a, "poor": math.ceil(0.05 * a), "good": math.ceil(0.1 * a), "great": math.ceil(0.15 * a),
            "excellent": math.ceil(0.2 * a)}.get(r.lower(), "Rating not recognised")

-----------------
"""

# https://www.codewars.com/kata/reviews/566186d5daed5a4c370000a7/groups/633c95644d947c0001db30f6
