# link: https://www.codewars.com/kata/57613fb1033d766171000d60

def uefa_euro_2016(teams, scores):
    match scores:
        case a, b if a > b:
            return f"At match {teams[0]} - {teams[1]}, {teams[0]} won!"
        case a, b if a < b:
            return f"At match {teams[0]} - {teams[1]}, {teams[1]} won!"
        case a, b if a == b:
            return f"At match {teams[0]} - {teams[1]}, teams played draw."

# I have been studying Python for two months.

'''
Best practices
--------------

def uefa_euro_2016(teams, scores):
    return f"At match {teams[0]} - {teams[1]}, {'teams played draw.' if scores[0] == scores[1] else teams[scores.index(max(scores))] + ' won!'}"

--------------

def uefa_euro_2016(teams, scores):
    s1, s2 = scores
    result = "teams played draw." if s1 == s2 else f"{teams[s1 < s2]} won!"
    return f"At match {teams[0]} - {teams[1]}, {result}"
    
--------------
'''