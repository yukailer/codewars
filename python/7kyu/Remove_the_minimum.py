def remove_smallest(numbers):
    notnumbers=numbers.copy()
    if len(notnumbers)==0:
        return []
    for i in notnumbers:
        if i==min(notnumbers):
            notnumbers.remove(i)
            return notnumbers

'''
### best solution ###
def remove_smallest(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    return a
'''

