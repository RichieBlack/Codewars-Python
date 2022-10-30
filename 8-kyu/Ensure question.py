def ensure_question(s):
    return s + '?' if '?' not in s else s

# I have been studying Python for two months.

'''
Best practices
--------------
def ensure_question(s):
    return s.rstrip('?') + '?'
    
--------------

def ensure_question(s):
    if not s.endswith("?"):
        return s + "?"
    return s

--------------
def ensure_question(s):
    return s if s.endswith('?') else s + '?'
'''

# https://www.codewars.com/kata/reviews/5ff7156ce4f95100016449b9/groups/634753119f0a14000143270d