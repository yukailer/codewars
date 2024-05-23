def array_diff(a, b):
    for i in b:
        a = list(filter((i).__ne__, a))
    return(a)

'''
### best solution
def array_diff(a, b):
    return [x for x in a if x not in b]
'''
