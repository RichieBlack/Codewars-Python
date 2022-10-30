"""
@File    : UEFA EURO 2016 .py
@Author  : Richie Black
@Time    : 26.10.2022 21:52

I have been learning Python since August 2022.
"""


def uefa_euro_2016(teams, scores):
    match scores:
        case a, b if a > b:
            return f"At match {teams[0]} - {teams[1]}, {teams[0]} won!"
        case a, b if a < b:
            return f"At match {teams[0]} - {teams[1]}, {teams[1]} won!"
        case a, b if a == b:
            return f"At match {teams[0]} - {teams[1]}, teams played draw."


'''
Best practices
--------------

def uefa_euro_2016(teams, scores):
    return f"At match {teams[0]} - {teams[1]}, {'teams played draw.' if scores[0] == scores[1] else teams[
            scores.index(max(scores))] + ' won!'}"

--------------

def uefa_euro_2016(teams, scores):
    s1, s2 = scores
    result = "teams played draw." if s1 == s2 else f"{teams[s1 < s2]} won!"
    return f"At match {teams[0]} - {teams[1]}, {result}"
    
--------------
'''

# https://www.codewars.com/kata/reviews/6037cf6a96b0260001cd9670/groups/6346aeea7b911e0001bc6941
