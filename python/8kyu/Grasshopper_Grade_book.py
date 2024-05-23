from statistics import mean
def get_grade(s1, s2, s3):
    # Code here
    avg=int(mean([s1,s2,s3]))
    if avg in range(90,101): return "A"
    if avg in range(80,91): return "B"
    if avg in range(70,81): return "C"
    if avg in range(60,71): return "D"
    else: return "F"

'''
### best solution ###
def get_grade(*s):
    return 'FFFFFFDCBAA'[sum(s)//30]
'''
