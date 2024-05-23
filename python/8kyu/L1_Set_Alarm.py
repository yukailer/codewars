def set_alarm(employed, vacation):
    return True if employed and not vacation else False

'''
### best solution ###
def set_alarm(employed, vacation):
    return employed and not vacation
'''
