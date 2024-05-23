def find_outlier(integers):
    def even(x):
        return 1 if x%2==0 else 0 
    
    def outlier(z,e):
        for i in integers:
            if e==1 and even(i) == 0:
                return i
            if e==0 and even(i) == 1:
                return i
            
    counter_e=0
    counter_o=0
    for i in integers[:3]:
        if even(i)==1:
            counter_e+=1
        else:
            counter_o+=1
    if counter_e>counter_o:
        return outlier(integers,1)
    else:
        return outlier(integers,0) 

'''
### best solutions ###
# shot but inefficient
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]

def find_outlier(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)

def find_outlier(l):
    p=[n%2 for n in l];return l[p.index(p.count(1)<2)]

'''
