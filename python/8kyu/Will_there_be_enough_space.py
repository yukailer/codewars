def enough(cap, on, wait):
    return 0 if cap-on-wait>0 else abs(cap-on-wait)

'''
### best solution ###
def enough(cap, on, wait):
    return max(0, wait - (cap - on))
'''
