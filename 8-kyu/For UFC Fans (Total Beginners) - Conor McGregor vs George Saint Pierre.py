# link: https://www.codewars.com/kata/reviews/582db0dda50d69ab8c000128/groups/582df0a1560ca747360000ae

def quote(fighter):
    if fighter.lower() == 'george saint pierre':
        return "I am not impressed by your performance."
    else:
        return "I'd like to take this chance to apologize.. To absolutely NOBODY!"

# I have been studying Python for one month.

'''
Best practices
--------------

statements = {
    'george saint pierre': "I am not impressed by your performance.",
    'conor mcgregor': "I'd like to take this chance to apologize.. To absolutely NOBODY!"
}

def quote(fighter):
    return statements[fighter.lower()]

--------------

def quote(fighter):
    return ["I am not impressed by your performance.",\
    "I'd like to take this chance to apologize.. To absolutely NOBODY!"][fighter.lower() == 'conor mcgregor']

--------------

def quote(fighter):
    return "I am not impressed by your performance." if "i" in fighter else "I'd like to take this chance to apologize.. To absolutely NOBODY!"

--------------
'''
