import math 
def is_square(n):    
    if n>=0 and int(math.sqrt(n))**2 == n:  
        return True
    else:
        return False

