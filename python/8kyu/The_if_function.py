def _if(bool, func1, func2):
    if bool == True: func1()
    else: func2()
    pass

def func1(): 
    print("True")
    
def func2(): 
    print("False")
