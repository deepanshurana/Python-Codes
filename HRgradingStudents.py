"""
To find the next multiple of x of n:
use formula (n + (x - n % x))
here x = 5
"""

def gradingStudents(grades):
    res = []
    for i in grades:
        if i >= 38:
            if(i + (5 - i % 5)-i < 3):   
                res.append(i + (5 - i % 5))
            else:
                res.append(i)
        else:
            res.append(i)
    return res

