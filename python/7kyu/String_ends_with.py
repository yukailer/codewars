def solution(text, ending):
    return text[-len(ending):]==ending

'''
### best solution ###
def solution(string, ending):
    return string.endswith(ending)
'''
