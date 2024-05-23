def duplicate_count(text):
    res=0
    text=text.lower()
    for i in text:
        if text.count(i)>1:
            res+=1
            text=text.replace(i, '')
    return res

'''
### best solution  ###
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])
'''
