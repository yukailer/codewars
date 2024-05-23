def divisors(integer):
    range_list=list(range(2,integer-1))
    for i in range_list[:]:
        if integer % i != 0:
            range_list.remove(i)
    if len(range_list)==0:
        return "%s is prime" %(integer)
    else:
        return range_list

'''
### best solutions ###
def divisors(n):
    return [i for i in xrange(2, n) if not n % i] or '%d is prime' % n

def divisors(num):
    l = [a for a in range(2,num) if num%a == 0]
    if len(l) == 0:
        return str(num) + " is prime"
    return l
'''
