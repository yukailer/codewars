import string
def printer_error(s):
    colors=string.ascii_lowercase[0:13]
    return str(sum(1 for i in s if i not in colors))+"/"+str(len(s))
