#https://www.codewars.com/kata/reviews/54a5cd6f8e5c31733e000013/groups/5fe6e4b0b259860001aea6eb

def are_you_playing_banjo(name):
    if name[0] == "r" or name[0] == "R":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"


# I have been studying Python for one month.

"""Best practices
-----------------

def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'

-----------------

def areYouPlayingBanjo(name):
    return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo"

-----------------

def areYouPlayingBanjo(name):
    if name.startswith('R') or name.startswith('r'):
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'

-----------------
"""
