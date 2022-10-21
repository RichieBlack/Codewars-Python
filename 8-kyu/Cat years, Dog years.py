"""
@File    : Cat years, Dog years.py 
@Author  : Richie Black
@Time    : 21.10.2022 21:42

I have been learning Python since August 2022.
"""


def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        cat_years = 15
        dog_years = 15
    if human_years == 2:
        cat_years = 24
        dog_years = 24
    if human_years > 2:
        cat_years = (human_years - 2) * 4 + 24
        dog_years = (human_years - 2) * 5 + 24
    return [human_years, cat_years, dog_years]


"""Best practices
-----------------

def human_years_cat_years_dog_years(human_years):
    catYears = 0
    dogYears = 0
    if human_years == 1:
        catYears += 15
        dogYears += 15
        return [human_years, catYears, dogYears]
    elif human_years == 2:
        catYears += 24
        dogYears += 24
        return [human_years, catYears, dogYears]
    elif human_years > 2:
        catYears += 24
        dogYears += 24
        years = human_years - 2
        catYears += years * 4
        dogYears += years * 5
        return [human_years, catYears, dogYears]
    return [0, 0, 0]

-----------------

def human_years_cat_years_dog_years(x):
    return [x, 24 + (x - 2) * 4 if (x != 1) else 15, 24 + (x - 2) * 5 if (x != 1) else 15]

-----------------

def human_years_cat_years_dog_years(n):
    cat_years = 15 + (9 * (n > 1)) + (4 * (n - 2) * (n > 2))
    dog_years = 15 + (9 * (n > 1)) + (5 * (n - 2) * (n > 2))
    return [n, cat_years, dog_years]

-----------------

def human_years_cat_years_dog_years(hy):
    return [hy, 16 + 4 * hy, 14 + 5 * hy] if hy > 1 else [1, 15, 15]
    
-----------------
"""

# https://www.codewars.com/kata/reviews/5a67b10993f7627b99002ee6/groups/632993293a67bb0001848084
