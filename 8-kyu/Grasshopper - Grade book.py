# link: https://www.codewars.com/kata/reviews/55e4892fa8095f4c6200000d/groups/55f80a7195f8e1c3bb00004d

def get_grade(s1, s2, s3):
    grade = (s1 + s2 + s3) / 3
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"


'''
Best practices
--------------

def get_grade(s1, s2, s3):
    m = (s1 + s2 + s3) / 3.0
    if 90 <= m <= 100:
        return 'A'
    elif 80 <= m < 90:
        return 'B'
    elif 70 <= m < 80:
        return 'C'
    elif 60 <= m < 70:
        return 'D'
    return "F"

--------------

def get_grade(s1, s2, s3):
    mean = sum([s1, s2, s3]) / 3
    if mean >= 90: return 'A'
    if mean >= 80: return 'B'
    if mean >= 70: return 'C'
    if mean >= 60: return 'D'
    return 'F'

--------------

def get_grade(s1, s2, s3):
    return {6: 'D', 7: 'C', 8: 'B', 9: 'A', 10: 'A'}.get((s1 + s2 + s3) / 30, 'F')

--------------

def get_grade(*s):
    return 'FFFFFFDCBAA'[sum(s) // 30]

--------------

scores = {10: 'A', 9: 'A', 8: 'B', 7: 'C', 6: 'D'}

def get_grade(*args):
    mean = sum(args) / len(args)
    return scores.get(mean // 10, 'F') 

--------------
'''
