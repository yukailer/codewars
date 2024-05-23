def bonus_time(salary, bonus):
    return "$"+str(salary*10) if bonus else "$"+str(salary)

'''
### best solution ###
def bonus_time(salary, bonus):
    return "${}".format(salary * (10 if bonus else 1))
'''
