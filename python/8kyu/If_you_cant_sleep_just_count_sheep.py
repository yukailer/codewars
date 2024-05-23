def count_sheep(n):
    res=""
    for i in range(1, n+1, 1):
        res=res + str(i) + " sheep..."
    return res

'''
### best solution  ####
def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1,n+1))
'''
