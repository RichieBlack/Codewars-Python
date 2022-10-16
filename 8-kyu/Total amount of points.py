# https://www.codewars.com/kata/reviews/5bb9109b16a8f195ea001643/groups/5e2d021b9632a90001b79ff9

def points(games):
    points = 0

    for i in range(len(games)):
        if games[i][0] > games[i][-1]:
            points += 3
        if games[i][0] == games[i][-1]:
            points += 1

    return points


# I have been studying Python for one month.

"""Best practices
-----------------

def points(games):
    count = 0
    for score in games:
        res = score.split(':')
        if res[0]>res[1]:
            count += 3
        elif res[0] == res[1]:
            count += 1
    return count

-----------------

def points(a):
    return sum((x >= y) + 2 * (x > y) for x, y in (s.split(":") for s in a))

-----------------

def points(games):
    return sum([0, 1, 3][1 + (g[0] > g[2]) - (g[0] < g[2])] for g in games)

-----------------
"""
